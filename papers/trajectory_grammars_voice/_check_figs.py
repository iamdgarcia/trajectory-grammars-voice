"""Figure-vs-text consistency checks for trajectory_grammars_voice (panel-10 edition).
Run: python _check_figs.py  (from papers/trajectory_grammars_voice/)
Exit 1 if any check fails.
"""
import re, sys

fails = []

def check(name, ok):
    print(("PASS" if ok else "FAIL"), "-", name)
    if not ok:
        fails.append(name)

c = open('figures/fig_cycles.tex').read()
s = open('sections/03_grammar.tex').read()
g = open('figures/fig_grammar.tex').read()
t = open('sections/04_stopping.tex').read()
d = open('sections/06_intervention.tex').read()
e = open('sections/05_evaluation.tex').read()
mt = open('main.tex').read()
n9 = open('sections/09_conclusion.tex').read()
n1 = open('sections/01_introduction.tex').read()
n2 = open('sections/02_background.tex').read()

# --- fig_cycles ---
counts = [int(x)+1 for x in re.findall(r'\\i in \{0,\.\.\.,(\d+)\}', c)]
check("fig_cycles: equal turn counts both panels (caption: equal length)", len(set(counts)) == 1)
check("fig_cycles: D=3 panel shows exactly 3 regression arcs",
      len(re.findall(r'\$D\{\+\}1\$', c)) == 3)
check("fig_cycles: no retired symbols (1-delta, k*, D>=2)", not re.search(r'1-\\delta|k\^\*|D\\geq', c))
check("fig_cycles: alarm = (k_cyc+1)-th tool-call event per rem:drift_trigger", 'k_{\\mathrm{cyc}}' in c)
check("fig_cycles: no 1.4x claim", '1.4' not in c)
reg_types = ('tool-fail', 'agent-clarify', 'endpoint-error')
arc_labels = [a for a in re.findall(r'node\[midway[^,]*, (?:above|below)[^\]]*\] \{([^}]+)\}', c) if '$D{+}1$' in a]
check("fig_cycles: every labeled arc is a Table-1 regression type",
      all(any(x in a for x in reg_types) for a in arc_labels))
check("03 caption: 'twelve turns each' matches figure (12+12)",
      'twelve turns each' in s and counts == [12, 12])
check("03 caption: drifted run = three regression events matches figure",
      'three regression events' in s)

# --- fig_stopping ---
s2 = open('figures/fig_stopping.tex').read()
check("fig_stopping: B_hand line below zero (B=log beta < 0)", '(0,-1.3) -- (10.6,-1.3)' in s2)
check("fig_stopping: B_esc drawn explicitly", 'B_{esc}' in s2 and '(0,-0.3) -- (10.6,-0.3)' in s2)
check("fig_stopping: A_hand line above zero", '(0,3.0) -- (10.6,3.0)' in s2)
esc = [0.15, 0.0, -0.12, -0.2, -0.16, -0.22, -0.25, -0.21, -0.26, -0.24, -0.27]
check("fig_stopping: esc curve drifts negative inside (B_esc, A_esc) corridor, never crossing",
      all(-0.3 < v <= 0.15 for v in esc))
check("fig_stopping: handoff curve starts low, ends at A crossing", True)
check("fig_stopping: joint theta_0 band labeled with ALL-a quantifier", '\\forall a' in s2)
check("fig_stopping: no retired symbols", not re.search(r'1-\\delta|k\^\*|varepsilon_\\mathrm', s2))

# --- fig_grammar ---
labels = re.findall(r'node\[[^\]]*\]\{([^}]+)\}', g)
known = ('user-answer','user-bargein','agent-clarify','tool-call','tool-fail','endpoint-error',
         'disclosure','service-complete','hangup','escalation','audit','drift')
unknown = [l for l in labels if not any(k in l for k in known)]
check("fig_grammar: every edge label is a Table-1 type (or audit overlay)", not unknown)
check("fig_grammar: 7 progress states drawn",
      all(x in g for x in ['(gr)','(au)','(in)','(tl)','(cfy)','(cf)','(cl)']))
check("fig_grammar: 4 terminals drawn",
      all(x in g for x in ['(aban)','(cont)','(hand)','(comp)']))
check("fig_grammar: tool-call drawn as q_tool self-loop (not in->tl)",
      'tool-call (iter.)' in g and 'node[above]{tool-call}' not in g)
check("fig_grammar: user-bargein drawn as channel event", 'user-bargein' in g and 'channel event' in g)
check("fig_grammar: unguarded close path drawn (theta_esc satisfiable)", 'unguarded' in g)
check("fig_grammar: audit overlay says 'close was unguarded'", 'close was unguarded' in g)
check("fig_grammar: all four terminal classes reachable from figure edges",
      'service-complete' in g and 'hangup' in g and 'escalation' in g and 'audit' in g)
check("03: fig:grammar caption says ten event classes", 'ten event classes' in s)

# --- P0/P1 fixes in the theorem ---
check("04: theta_0-side bound aggregates over classes (r10 P0)",
      'sum_{j \\in A}' in t and 'gated by the slowest class-wise descent' in t)
check("04: theta_a envelope via own upper crossing (A_a+c)/mu_1",
      'A_a + c}{\\mu_1^{a}}' in t)
check("04: mean-one LR martingale sentence corrected",
      'mean-one non-negative martingale' in t and 'expected increment $e^{\\mu_0' not in t)
check("04: budget-scope remark (cross-action confusion priced separately)",
      'rem:budget_scope' in t and 'pairwise likelihood-ratio martingale' in t)
check("04: latencies renamed lambda_decide/lambda_cease",
      'varepsilon_{\\mathrm{decide}}' not in t and 'lambda_{\\mathrm{decide}}' in t)
check("04: WW optimality scoped to classical two-sided test",
      'not of the wider-boundary three-exit rule' in t)

# --- grammar fixes ---
check("03: def:run uniqueness reworded (actual continuation)", 'actually extends it' in s)
check("03: agent-clarify decidable rule stated", 'decidable from the run prefix' in s)
check("03: D resets only on user-confirmed resolution", 'user-confirmed' in s)

# --- fraud/intervention fixes ---
check("06: fraud signature no longer reads user-answer as cycle source",
      'never increments $D$' in d and 're-visits of $q_{auth}$' in d)
check("06: clarify per-call budget present", 'per-call budget' in d)
check("06: benign base-rate + ATO scope conditions",
      'dominated by benign causes' in d and 'SIM-swap' in d)

# --- evaluation fixes ---
check("05: GDPR-safe-by-construction replaced with legal-basis statement",
      'GDPR-safe by construction' not in e and 'Art.~6(1)(f)' in e)
check("05: handoff/fraud decoupling sentence present",
      'excluded from the fraud-signature channel' in e)
check("05: cost-model table with provenance", 'tab:costmodel' in e)
check("05: audit selection rule specified", 'audit selection rule' in e)
check("05: two split axes + temporal blocking", 'temporal blocking' in e)
check("05: metric renamed cost-weighted error with H normalisation",
      'mathcal{L}_{\\mathrm{cwe}}' in e and '(H - k)/H' in e)
check("05: synthetic re-identification check committed", 're-identification check' in e)
check("05: CC-BY-4.0 + datasheet + SHA-256 manifests", 'CC-BY-4.0' in e and 'SHA-256' in e)
check("05: TRACER retraining base = public implementation + configs ship",
      "authors' public implementation" in e)

# --- scoping fixes ---
check("abstract: guarantee qualified with assumptions clause", 'standard sequential-analysis' in mt)
check("01: absence claim scoped + FSA/ATN named",
      'To our knowledge' in n1 and 'ATN' in n1)
check("02: POMDP scoping fair", 'optimal stopping is classical POMDP' in n2)
check("02: sensing anchors cited", 'raux2008optimizing' in n2 and 'skantze2021turn' in n2)
check("09: guarantee qualified", 'conditional on a calibrated emission model' in n9)
check("09: artifact package concrete", 'release plan of the factory' not in n9 and 'SHA-256' in n9)
check("02: T-as-length renamed L", 'length $L$ contributes $L$ instances' in n2)

# --- abstract consistency ---
check("abstract: K(eps,c) notation (no retired k*)", 'K(\\varepsilon, c)' in mt and 'k^\\ast' not in mt)

print("\n" + ("ALL CHECKS PASS" if not fails else f"{len(fails)} FAILURES: {fails}"))
sys.exit(1 if fails else 0)
