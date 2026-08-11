# Professional AI Skills (AIOS)

A cross-platform library of concise, composable skills for professional AI assistants. Each skill is a self-contained capability with explicit triggers, repeatable workflow, decision rules, failure modes, and quality checks.

> AIOS is not a collection of magic prompts. It is an open, testable operating layer for reliable professional work.

## Current release

The library now includes 112 production-ready skills across core reasoning, communication, business, enterprise IT, Microsoft 365, cybersecurity, leadership, research, software engineering, productivity, and AI product work. The roadmap continues with deeper examples, regression checks, and release packaging.

## Install into Claude Code

Clone the repo and mount all 112 skills. Two options:

```bash
# Available in every project (installs into ~/.claude/skills)
python3 scripts/install_skills.py --global

# Or ship them with a specific repo (creates ./.claude/skills, travels with the clone)
python3 scripts/install_skills.py
```

Then invoke any skill by name in Claude Code, e.g. `/risk-analysis` or `/threat-modeling`.
Working inside a clone of this repo, the bundled `.claude/skills/` mount means the skills
are already available with no install step.

## Quick start (any assistant)

1. Browse the [catalog](docs/catalog.md).
2. Copy a skill folder into a supported skills directory, or upload `SKILL.md` as project knowledge.
3. Invoke it, for example: `Use $risk-analysis to assess this proposal.`
4. Combine only the few skills needed.

See [platform guidance](platform/README.md).

## Repository map

- `skills/`: reusable capability folders
- `frameworks/`: shared analytical methods
- `templates/`: output structures
- `playbooks/`: multi-stage workflows
- `personas/`: legitimate stakeholder lenses
- `evaluations/`: rubrics and regression cases
- `platform/`: loading guidance
- `docs/`: specifications and governance

## Validate

```bash
python3 scripts/validate_repository.py   # structure and frontmatter
python3 scripts/run_checks.py            # per-skill quality contract + mirror sync
```

`run_checks.py` enforces that every skill has a concrete trigger, a real multi-step workflow,
a bounded output, a worked example, named failure modes, resolving cross-links, and that the
`.claude/skills/` mount matches the canonical `skills/` source. Both run in CI on every push.

Read the [skill specification](docs/skill-specification.md), [style guide](docs/style-guide.md), and [contribution guide](CONTRIBUTING.md).

## License

[MIT](LICENSE)
