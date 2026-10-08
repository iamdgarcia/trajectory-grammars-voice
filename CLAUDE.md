# AI Research Factory

## Build Commands

```bash
# Compile any paper (run from the paper's directory)
cd papers/<paper_slug>/
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex

# Package for arXiv upload
zip -r ../<paper_slug>_arxiv.zip main.tex main.bib sections/ figures/
```

## Paper Factory Pipeline

### Trigger

To generate a new paper: say `"Write a new paper on <topic>"`

### Pipeline Stages (fully automatic)

#### Stage 1 — Gap Detection
1. Read all `knowledge_base/topics/<topic>/papers/*.md`
2. Read `knowledge_base/topics/<topic>/gaps.md`
3. If fewer than 10 paper entries exist for the topic: run `deep-research` skill to populate first
4. Filter entries: `gap_score >= 4` AND `conceptual: true`
5. Cross-reference `gaps.md` — skip gaps already marked as addressed
6. Select the highest-gap conceptual opportunity
7. Write contribution statement + working title to `papers/<slug>/OUTLINE.md`

#### Stage 2 — Outline
Generate section structure in `OUTLINE.md`:
- Introduction (motivation, gap statement, contributions, paper structure)
- Background (taxonomy of relevant work — cite KB entries)
- Framework/Taxonomy (the paper's conceptual contribution)
- Analysis (implications, theoretical properties — TikZ diagrams)
- Open Problems (future directions)
- Discussion (limitations, scope)
- Conclusion

#### Stage 3 — LaTeX Writing
- Copy `templates/arxiv_preprint/` to `papers/<slug>/` (or specified venue template)
- Write each section as a `.tex` file in `sections/`
- Rules:
  - ALL conceptual figures must be TikZ — no external images except icons
  - All claims must have `\cite{}` backed by an entry in `knowledge_base/`
  - One sentence per line in `.tex` files
  - Use `\input{}` not `\include{}`
- Compile to verify: `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`
- Target: 0 errors, <=5 warnings

#### Stage 4 — Peer Review Simulation
Spawn a multi-agent review panel:
- **Chief Editor**: synthesises final decision from reviewer scores
- **Reviewer 1**: methodology expert
- **Reviewer 2**: domain expert (the paper's specific topic)
- **Reviewer 3**: writing and presentation
- **Reviewer 4**: related work coverage

Each reviewer produces:
- Score (1-10)
- List of mandatory revisions (blocking acceptance)
- List of optional suggestions

Chief Editor produces:
- Decision: Accept / Minor Revision / Major Revision / Reject
- Consolidated mandatory revision list

#### Stage 5 — Revision Loop
- Apply ALL mandatory revisions
- Re-run Stage 4
- Repeat until Chief Editor decision is Accept or Minor Revision
- Cap at 5 rounds — if not accepted by round 5, flag for human review

#### Stage 6 — arXiv Prep
- Clean compile: 0 errors
- Package: `zip -r papers/<slug>_arxiv.zip papers/<slug>/main.tex papers/<slug>/main.bib papers/<slug>/sections/ papers/<slug>/figures/`
- Output: `<slug>_arxiv.zip` ready for upload to arxiv.org under cs.AI (primary), cs.CR (cross-list)

## Knowledge Base Conventions

- Paper entries: `knowledge_base/topics/<topic>/papers/<cite_key>.md`
- Schema: see `knowledge_base/SCHEMA.md`
- Gap tracking: `knowledge_base/topics/<topic>/gaps.md`
- Master index: `knowledge_base/INDEX.md`

## LaTeX Conventions

- TikZ for ALL diagrams — no matplotlib, no external plot images
- `natbib` + `\citep{}`/`\citet{}` for arxiv_preprint template
- `\cite{}` for ieee_trans and acm_csur templates
- One sentence per line
- `\input{}` only, never `\include{}`

## Author

Daniel Garcia Pena — info@iamdgarcia.com — ORCID: 0000-0002-1456-4785
Always publish to arXiv: cs.AI (primary), cs.CR (cross-list if safety-focused).
