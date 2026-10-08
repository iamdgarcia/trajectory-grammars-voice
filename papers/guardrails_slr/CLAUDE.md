# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

This is a LaTeX research paper on **AI guardrails** — the document does not yet exist and must be built from scratch. The workflow is: (1) research the state of the art, (2) identify the contribution gap, (3) write the paper in LaTeX.

**Author:** Daniel García Peña (info@iamdgarcia.com)  
**ORCID:** https://orcid.org/0000-0002-1456-4785

## Build Commands

```bash
# Compile the paper (run twice for cross-references)
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex

# Quick single-pass compile (no bibliography update)
pdflatex main.tex

# Clean auxiliary files
rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk *.synctex.gz
```

## Repository Structure (target layout)

```
main.tex          # master document — \input{} sections from sections/
main.bib          # BibTeX bibliography (collect references here)
sections/         # one .tex file per paper section
figures/          # PDF/PNG/EPS figures (prefer PDF for vector)
tables/           # complex tables as separate .tex files (optional)
```

## LaTeX Conventions

- Use `\input{}` (not `\include{}`) for section files to avoid page breaks between fragments.
- Bibliography: BibTeX (`bibtex`) with `natbib` and `\citep{}`/`\citet{}` citation commands.
- Figures: always `\includegraphics[width=\linewidth]{figures/foo}` — omit extension so pdflatex picks the best format.
- Keep one sentence per line in `.tex` files — makes git diffs readable.
- Target venue will determine the document class (IEEE, ACM, Springer LNCS, etc.) — confirm with user before committing to one.

## Research Workflow

1. Use `deep-research` skill to survey the AI guardrails literature before writing.
2. Identify contribution gap — what problem is insufficiently addressed?
3. Draft outline → get user approval → write sections incrementally.
4. Validate every claim has a `\cite{}` backing it before the paper is considered draft-complete.

## Skills to Use

- `/deep-research` — for literature survey and state-of-the-art analysis on guardrails, safety, content filtering, LLM alignment.
- `document-skills:pdf` — if generating or manipulating PDFs (e.g., figure conversion).
- `graphify` — to visualize the knowledge graph of the research space.
- `superpowers:brainstorming` — before defining the paper's contribution or structure.
