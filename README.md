# Professional AI Skills (AIOS)

A cross-platform library of concise, composable skills for professional AI assistants. Each skill is a self-contained capability with explicit triggers, repeatable workflow, decision rules, failure modes, and quality checks.

> AIOS is not a collection of magic prompts. It is an open, testable operating layer for reliable professional work.

## Current release

The foundation includes 20 production-ready skills across core reasoning, communication, business, and research. The roadmap expands to 100 skills plus frameworks, templates, playbooks, personas, evaluations, and platform packs.

## Quick start

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
python3 scripts/validate_repository.py
```

Read the [skill specification](docs/skill-specification.md), [style guide](docs/style-guide.md), and [contribution guide](CONTRIBUTING.md).

## License

[MIT](LICENSE)
