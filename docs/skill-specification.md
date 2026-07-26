# Skill Specification

## Required layout

```text
skill-name/
├── SKILL.md
└── agents/openai.yaml
```

Optional `scripts/`, `references/`, and `assets/` must support execution. Do not add per-skill READMEs or changelogs.

`SKILL.md` frontmatter contains only `name` and `description`; the name matches the folder and the description states capability plus concrete triggers.

A production skill defines inputs, repeatable workflow, observable decision rules, output contract, quality checks, failure recovery, example, evaluation criteria, and related skills where useful. Do not add sections merely to satisfy a template.

Assume general model knowledge. Include specialized process, selection rules, and constraints. Prefer one lead skill and at most two supporting skills; the lead owns the final output. Do not assume a model, connector, private memory, or hidden tool.

Acceptance requires a distinct capability, clear triggering, reusable workflow, safe uncertainty handling, bounded output, repository validation, and representative forward testing.
