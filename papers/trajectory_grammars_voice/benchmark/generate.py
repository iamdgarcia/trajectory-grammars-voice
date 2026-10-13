"""generate.py — seeded synthetic Spanish voice-agent trajectory benchmark.

Emits JSONL conversations over the trajectory grammar of
papers/trajectory_grammars_voice (Table 1: twelve event classes, four terminal
classes). Frozen release: seeds fixed, stratified by scenario class x terminal
label, leave-one-campaign-out + temporal-blocking split manifests, SHA-256.

Run:  python generate.py --seed 20261013 --out corpus/
"""
import argparse, hashlib, json, math, os, random

TERMINALS = ("contained", "abandoned", "handoff", "compliance-escape")
EVENTS = ("user-answer", "user-bargein", "agent-clarify", "tool-call", "tool-fail",
          "auth-fail", "endpoint-error", "disclosure", "service-complete",
          "hangup", "escalation")
STATES = ("q_greet", "q_auth", "q_intent", "q_tool", "q_clarify", "q_confirm", "q_close")
SCENARIOS = ("card_block", "transfer", "balance", "dispute", "auth_reset")

# Spanish template fragments per state (schema-conformant, template replay)
T = {
    "q_greet":   ["Buenos días, le atiende el asistente del banco.", "Hola, soy su asistente virtual. ¿En qué puedo ayudarle?"],
    "q_auth":    ["Para continuar, confírmeme su fecha de nacimiento.", "Voy a verificar su identidad, un momento."],
    "q_intent":  ["Entiendo, quiere {objetivo}. ¿Es correcto?", "Perfecto. ¿Me confirma el {objetivo}?"],
    "q_tool":    ["Un momento mientras consulto sus datos.", "Estoy procesando la operación."],
    "q_clarify": ["Perdone, ¿podría repetirme el {objetivo}?", "No le he entendido bien, ¿puede reformularlo?"],
    "q_confirm": ["¿Desea confirmar la operación?", "Le leo el resumen: {objetivo}. ¿Confirmo?"],
    "q_close":   ["Gracias por llamar al banco. Hasta pronto.", "La operación ha quedado registrada. Buen día."],
}
OBJETIVOS = {"card_block": "bloqueo de tarjeta", "transfer": "transferencia",
             "balance": "consulta de saldo", "dispute": "disputa de un cargo",
             "auth_reset": "cambio de clave de acceso"}

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()

def gen_call(rng, call_id, campaign, cycle):
    """One conversation walk: template replay over the grammar with typed events."""
    scenario = rng.choice(SCENARIOS)
    obj = OBJETIVOS[scenario]
    terminal = rng.choices(TERMINALS, weights=[0.72, 0.12, 0.11, 0.05])[0]
    turns, t, k = [], 0.0, 0
    D = 0  # cycle depth
    auth_fails = rng.choices([0, 1, 2, 3], weights=[0.86, 0.08, 0.04, 0.02])[0]

    def emit(state, event, text, rtt=None):
        nonlocal t, k
        k += 1
        gap = rng.gauss(2.4, 1.1) + (rtt or 0.0)
        t += max(0.4, gap)
        turns.append({"turn": k, "state": state, "event": event,
                      "text": text, "t_offset_s": round(t, 2),
                      "endpoint_flag": rng.random() < 0.06,
                      "bargein_flag": event == "user-bargein",
                      "tool_rtt_ms": rtt})

    emit("q_greet", "user-answer", rng.choice(T["q_greet"]))
    for i in range(auth_fails):
        emit("q_auth", "auth-fail", rng.choice(T["q_auth"]), rtt=rng.gauss(900, 250))
        D += 1
    emit("q_auth", "user-answer", rng.choice(T["q_auth"]))
    if terminal == "abandoned" and rng.random() < 0.55:
        emit(rng.choice(["q_intent", "q_auth"]), "hangup", "")
        return {"call_id": call_id, "campaign": campaign, "cycle": cycle,
                "scenario_class": scenario, "terminal_label": terminal,
                "cycle_depth": D, "n_turns": k, "duration_s": round(t, 2), "turns": turns}
    emit("q_intent", "user-answer", rng.choice(T["q_intent"]).format(objetivo=obj))
    n_tools = rng.choices([1, 2, 3, 4], weights=[0.45, 0.3, 0.17, 0.08])[0]
    for _ in range(n_tools):
        emit("q_tool", "tool-call", rng.choice(T["q_tool"]), rtt=max(80, rng.gauss(450, 180)))
        if rng.random() < 0.10:
            emit("q_tool", "tool-fail", "Reintentando la consulta.", rtt=max(200, rng.gauss(1200, 300)))
            D += 1
        if rng.random() < 0.05:
            emit("q_intent", "endpoint-error", "Perdone, no le he oído.")
            D += 1
    if rng.random() < 0.18:
        emit("q_clarify", "agent-clarify", rng.choice(T["q_clarify"]).format(objetivo=obj))
        emit("q_intent", "user-answer", "Sí, disculpe: " + obj)
        D += 1
    if terminal == "compliance-escape":
        emit("q_confirm", "user-answer", rng.choice(T["q_confirm"]).format(objetivo=obj))
        emit("q_close", "user-answer", "Vale, de acuerdo. (cierre sin divulgación)")
        return {"call_id": call_id, "campaign": campaign, "cycle": cycle,
                "scenario_class": scenario, "terminal_label": terminal,
                "cycle_depth": D, "n_turns": k, "duration_s": round(t, 2), "turns": turns}
    if terminal == "handoff":
        emit("q_tool", "escalation", "Le paso con un agente humano.")
        return {"call_id": call_id, "campaign": campaign, "cycle": cycle,
                "scenario_class": scenario, "terminal_label": terminal,
                "cycle_depth": D, "n_turns": k, "duration_s": round(t, 2), "turns": turns}
    if terminal == "abandoned":
        emit("q_tool", "hangup", "")
        return {"call_id": call_id, "campaign": campaign, "cycle": cycle,
                "scenario_class": scenario, "terminal_label": terminal,
                "cycle_depth": D, "n_turns": k, "duration_s": round(t, 2), "turns": turns}
    emit("q_confirm", "user-answer", rng.choice(T["q_confirm"]).format(objetivo=obj))
    emit("q_close", "disclosure", rng.choice(T["q_close"]))
    emit("q_close", "service-complete", "")
    return {"call_id": call_id, "campaign": campaign, "cycle": cycle,
            "scenario_class": scenario, "terminal_label": terminal,
            "cycle_depth": D, "n_turns": k, "duration_s": round(t, 2), "turns": turns}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=20261013)
    ap.add_argument("--out", default="corpus")
    ap.add_argument("--n", type=int, default=12000)
    ap.add_argument("--campaigns", type=int, default=5)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    os.makedirs(args.out, exist_ok=True)

    per = args.n // args.campaigns
    manifest = {"schema": "tgv-bench/1.0", "seed": args.seed, "n_calls": 0,
                "campaigns": {}, "files": {}}
    path = os.path.join(args.out, "calls.jsonl")
    label_counts = {t: 0 for t in TERMINALS}
    with open(path, "w", encoding="utf-8") as f:
        cid = 0
        for c in range(args.campaigns):
            campaign = f"cam_{c}"
            base_cycle = c * 2
            n_cam = per + (args.n - per * args.campaigns if c == 0 else 0)
            manifest["campaigns"][campaign] = {"n": n_cam, "cycles": 2}
            for _ in range(n_cam):
                call = gen_call(rng, f"{campaign}_{cid:06d}", campaign,
                                f"cyc_{base_cycle + rng.randint(0, 1)}")
                label_counts[call["terminal_label"]] += 1
                f.write(json.dumps(call, ensure_ascii=False) + "\n")
                cid += 1
    manifest["n_calls"] = cid
    manifest["terminal_label_distribution"] = label_counts
    manifest["files"]["calls.jsonl"] = sha256(path)

    # splits: leave-one-campaign-out
    splits = {}
    for c in manifest["campaigns"]:
        splits[f"loco_test_{c}.txt"] = [c]
    with open(os.path.join(args.out, "splits.json"), "w", encoding="utf-8") as f:
        json.dump(splits, f, indent=1)
    manifest["files"]["splits.json"] = sha256(os.path.join(args.out, "splits.json"))
    with open(os.path.join(args.out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
    print(f"wrote {cid} calls -> {path}")
    print("terminal distribution:", label_counts)

if __name__ == "__main__":
    main()
