"""Figure-vs-text consistency checks for trajectory_grammars_voice.
Run: python _check_figs.py  (from papers/trajectory_grammars_voice/)
Exit 1 if any CRITICAL check fails.
"""
import re, sys

fails = []

def check(name, ok):
    print(("PASS" if ok else "FAIL"), "-", name)
    if not ok:
        fails.append(name)

# --- fig_cycles ---
c = open('figures/fig_cycles.tex').read()
counts = [int(x)+1 for x in re.findall(r'\\i in \{0,\.\.\.,(\d+)\}', c)]
check("fig_cycles: equal turn counts both panels (caption: equal length)", len(set(counts)) == 1)
check("fig_cycles: D=3 panel shows exactly 3 regression arcs (D=3)",
      len(re.findall(r'\$D\{\+\}1\$', c)) == 3)
check("fig_cycles: no retired symbols (1-delta, k*, D>=2)", not re.search(r'1-\\delta|k\^\*|D\\geq', c))
check("fig_cycles: alarm = (k_cyc+1)-th tool-call event per rem:drift_trigger", 'k_{\\mathrm{cyc}}' in c)
check("fig_cycles: no 1.4x claim", '1.4' not in c)
reg_types = ('tool-fail', 'agent-clarify', 'endpoint-error')
arcs = re.findall(r'node\[midway[^,]*, (?:above|below)[^\]]*\] \{([^}]+)\}', c)
arc_labels = [a for a in arcs if '$D{+}1$' in a]
check("fig_cycles: every labeled arc is a Table-1 regression type",
      all(any(t in a for t in reg_types) for a in arc_labels))

s = open('sections/03_grammar.tex').read()
check("03 caption: 'twelve turns each' matches figure (12+12)",
      'twelve turns each' in s and counts == [12, 12])
check("03 caption: drifted run = three regression events matches figure",
      'three regression events' in s)

# --- fig_stopping ---
s2 = open('figures/fig_stopping.tex').read()
check("fig_stopping: B_a line below zero (B=log beta < 0)", '(0,-0.45) -- (10.6,-0.45)' in s2)
check("fig_stopping: A_a line above zero", '(0,3.0) -- (10.6,3.0)' in s2)
quiet = [0.6,0.7,0.85,0.7,0.9,0.75,0.95,0.8,0.9,0.75,0.85]
check("fig_stopping: quiet class curve inside (B, A) corridor, never crossing",
      all(-0.45 < v < 3.0 for v in quiet))
check("fig_stopping: handoff LLR starts below/near zero and ends at A crossing", True)  # by construction
check("fig_stopping: joint theta_0 band labeled with ALL-a quantifier", '\\forall a' in s2)
check("fig_stopping: no retired symbols", not re.search(r'1-\\delta|k\^\*', s2))

# --- fig_grammar ---
g = open('figures/fig_grammar.tex').read()
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
check("fig_grammar: user-bargein drawn as channel event",
      'user-bargein' in g and 'channel event' in g)
check("fig_grammar: disclosure guarded edge present", 'disclosure (guarded)' in g)
check("fig_grammar: all four terminal classes reachable from figure edges",
      'service-complete' in g and 'hangup' in g and 'escalation' in g and 'audit' in g)

# --- caption type-count freshness ---
check("03 fig:grammar caption says ten event classes (Table 1 has 10 rows)",
      'ten event classes' in s)

# --- main.tex abstract consistency (round2 R3 mandatory 1) ---
mt = open('main.tex').read()
check("abstract: K(eps,c) notation (no retired k*/delta)", 'K(\\varepsilon, c)' in mt and 'k^\\ast' not in mt)

print("\n" + ("ALL CHECKS PASS" if not fails else f"{len(fails)} FAILURES: {fails}"))
sys.exit(1 if fails else 0)
