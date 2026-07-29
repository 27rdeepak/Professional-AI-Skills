# Professional AI Skills (AIOS)

AIOS is a vendor-neutral library of **112 structured skills** for professional AI-assisted work. It covers reasoning, executive communication, business analysis, enterprise IT, Microsoft 365, cybersecurity, leadership, research, software engineering, productivity, and AI product development.

Each skill packages a capability into reusable instructions with:

- clear trigger conditions
- required inputs
- a repeatable workflow
- decision and safety rules
- a defined output contract
- quality checks and failure handling
- user-facing metadata for compatible ChatGPT and Codex skill interfaces

> AIOS is an instruction and workflow library—not a collection of magic prompts, an autonomous agent platform, or a guarantee of factual accuracy.

## Current scope

| Category | Skills |
|---|---:|
| Business | 15 |
| AI product | 13 |
| Core reasoning | 13 |
| Communication | 11 |
| Software engineering | 11 |
| Research | 10 |
| Productivity | 9 |
| Cybersecurity | 8 |
| Microsoft 365 | 8 |
| Enterprise IT | 7 |
| Leadership | 7 |
| **Total** | **112** |

The [catalog](docs/catalog.md) highlights selected enterprise, security, Microsoft 365, business, leadership, and AI-product skills. The complete collection is available under [`skills/`](skills/).

## What the repository contains

```text
skills/<category>/<skill-name>/
├── SKILL.md
└── agents/
    └── openai.yaml
```

- `SKILL.md` contains the trigger description and operating instructions.
- `agents/openai.yaml` provides display metadata and a default invocation prompt.
- Optional `references/`, `scripts/`, and `assets/` should be included only when they materially support execution.

The wider repository adds:

- [`frameworks/`](frameworks/) — shared analytical methods such as RICE, SWOT, risk matrices, and premortems
- [`templates/`](templates/) — reusable output structures for briefs, reports, decisions, incidents, and reviews
- [`playbooks/`](playbooks/) — coordinated workflows spanning multiple stages or skills
- [`personas/`](personas/) — stakeholder lenses such as CIO, CISO, CFO, and enterprise architect
- [`evaluations/`](evaluations/) and [`tests/`](tests/) — quality rubrics, failure modes, and representative regression cases
- [`platform/`](platform/) — guidance for using selected skills with ChatGPT, Claude, Gemini, Cursor, Copilot, and Codex
- [`docs/`](docs/) — architecture, skill specification, quality model, and contribution standards

## How to use the skills

1. Choose one **lead skill** that owns the final output.
2. Add no more than one or two supporting skills unless the task genuinely requires them.
3. Load or attach the selected skill folder using the guidance for your AI platform.
4. Invoke the skill explicitly, for example:

```text
Use $risk-analysis to assess this proposal and identify the decision, evidence gaps, downside scenarios, and recommended next test.
```

5. Supply the real objective, audience, constraints, evidence, and desired output format.
6. Review high-impact results before using them for financial, legal, security, employment, or operational decisions.

See the [platform guidance](platform/README.md) for loading patterns. Platform support differs: some products can recognize skill metadata, while others treat `SKILL.md` as attached instructions or project knowledge.

## Quality and maturity

All 112 skill folders pass the repository’s **structural validation**, including:

- valid YAML frontmatter
- matching skill and folder names
- required trigger language
- matching `agents/openai.yaml`
- repository layout and minimum documentation checks

Structural validation does **not** prove domain accuracy, platform compatibility, or production effectiveness. Skill depth currently varies: newer enterprise, security, Microsoft 365, leadership, and AI-governance skills contain more domain-specific procedures, while some earlier skills still require deeper workflows and forward testing. The [roadmap](ROADMAP.md) tracks that work.

Use the [quality model](docs/quality-model.md), [evaluation rubric](evaluations/skill-evaluation-rubric.md), and [regression suite](tests/regression-suite.md) when assessing or extending a skill.

## Validate the repository

```bash
python3 scripts/validate_repository.py
```

The validator checks repository structure and metadata. It does not execute every workflow or independently verify domain claims.

## Contributing

Before adding a skill:

1. Check for overlap with an existing capability.
2. Use a lowercase hyphenated folder and matching skill name.
3. Keep frontmatter limited to `name` and `description`.
4. Define concrete triggers, workflow, decisions, outputs, failure handling, and evaluation criteria.
5. Add matching `agents/openai.yaml`.
6. Run the repository validator and representative forward tests.

Read the [skill specification](docs/skill-specification.md), [style guide](docs/style-guide.md), and [contribution guide](CONTRIBUTING.md).

## License

Licensed under the [MIT License](LICENSE).
