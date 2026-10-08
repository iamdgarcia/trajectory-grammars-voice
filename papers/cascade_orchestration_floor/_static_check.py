import pathlib
import re
import sys

root = pathlib.Path(".")
bib = (root / "main.bib").read_text(encoding="utf-8")
bib_keys = set(re.findall(r"@\w+\{([\w:]+),", bib))

texts = {}
for f in list((root / "sections").glob("*.tex")) + list((root / "figures").glob("*.tex")):
    texts[f.name] = f.read_text(encoding="utf-8")
maintex = (root / "main.tex").read_text(encoding="utf-8")
alltext = "\n".join(texts.values()) + "\n" + maintex

labels = set(re.findall(r"\\label\{([\w:]+)\}", alltext))
refs = set(re.findall(r"\\ref\{([\w:]+)\}", alltext))
inputs = re.findall(r"\\input\{([^}]+)\}", alltext)
cites = set()
for m in re.findall(r"\\cite[pt]?\{([^}]+)\}", alltext):
    for part in m.split(","):
        cites.add(part.strip())

errs = []
undef = sorted(k for k in cites if k and k not in bib_keys)
if undef:
    errs.append("CITES NOT IN BIB: " + ", ".join(undef))
undef_refs = sorted(r for r in refs if r not in labels)
if undef_refs:
    errs.append("REFS WITHOUT LABEL: " + ", ".join(undef_refs))
for i in inputs:
    if not pathlib.Path(i + ".tex").exists():
        errs.append(f"INPUT MISSING: {i}")
for name, t in texts.items():
    o = len(re.findall(r"\\begin\{", t))
    c = len(re.findall(r"\\end\{", t))
    if o != c:
        errs.append(f"UNBALANCED {name}: {o} begin / {c} end")

print("bib keys:", len(bib_keys), "| labels:", len(labels), "| refs:", len(refs),
      "| inputs:", len(inputs), "| cites:", len(cites))
if errs:
    for e in errs:
        print("ERR:", e)
    sys.exit(1)
print("STATIC CHECK OK")
