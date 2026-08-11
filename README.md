# Professional AI Skills (AIOS)

**112 professional AI skills — every one tested against a quality contract, installable into Claude Code in one command.**

[![Validate](https://github.com/27rdeepak/Professional-AI-Skills/actions/workflows/validate.yml/badge.svg)](https://github.com/27rdeepak/Professional-AI-Skills/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-112-brightgreen)

A cross-platform library of concise, composable skills for professional AI assistants. Each skill is a self-contained capability with explicit triggers, a repeatable workflow, decision rules, failure modes, and a worked example — covering reasoning, communication, business, cybersecurity, enterprise IT, Microsoft 365, leadership, research, software engineering, productivity, and AI product work.

> **What this is:** an open, testable operating layer that makes AI produce decision-useful, structured professional work.
> **What it isn't:** a bag of magic prompts. Every skill is a defined procedure, and CI proves it meets the bar.

## Why it's different

- **Tested, not vibes.** A validator and a forward-test runner enforce that *every* skill has concrete triggers, a real multi-step workflow, a bounded output, a worked example, named failure modes, and resolving cross-links. CI fails if any skill regresses.
- **Cross-platform.** Ships as Claude Code skills and OpenAI agent metadata; the `SKILL.md` works as project knowledge in any assistant.
- **One-command install.** Mount all 112 skills into Claude Code globally or per-repo.

## See the difference

These illustrate the *shape* of what a skill changes — from a plausible-sounding answer to a decision-useful one.

<details open>
<summary><b>$premortem-analysis</b> — before committing to a plan</summary>

**Prompt:** *"Will our Q4 platform migration go okay? The team is confident."*

**Raw assistant** → "It should go well if you plan carefully, test thoroughly, and communicate with stakeholders. Make sure to have backups and monitor closely."

**With `$premortem-analysis`** → *assume it already failed by year-end, then work backward:*

| Failure mode | Mechanism | Preventive control | Owner |
|---|---|---|---|
| Rollback never works | Rollback path untested before cutover | Rehearse rollback on a prod copy | Platform lead |
| Data integrity loss | Dual-write drift at cutover | Reconciliation gate before switch | Data eng |
| Adoption stalls | Teams keep the old tool | Cutover date + old-tool freeze | Eng managers |

**Bottom line:** the untested rollback is the top undetected risk — gate go/no-go on a rehearsal.
</details>

<details>
<summary><b>$vulnerability-management</b> — prioritizing security work</summary>

**Prompt:** *"We have 200 scanner findings. What do we patch first?"*

**Raw assistant** → "Start with the Critical (CVSS 9+) vulnerabilities, then High, then Medium."

**With `$vulnerability-management`** → separates *severity* from *risk*:

- A CVSS 9.8 on an isolated internal host ranks **below** a 7.5 on an internet-facing service.
- Rank by exploitability × asset criticality × exposure, enriched with active-exploit intelligence.
- Output: a risk-based order, the top bottleneck class, and an explicit "accept with exception" list — not a CVSS sort.

**Bottom line:** patch the internet-facing, actively-exploited 7.5 today; the isolated 9.8 can wait behind a compensating control.
</details>

<details>
<summary><b>$executive-writer</b> — briefing a leader</summary>

**Prompt:** *"Write an update about our launch slipping two weeks."*

**Raw assistant** → three paragraphs of background, the actual slip buried in paragraph two, no clear ask.

**With `$executive-writer`** → decision-first memo:

> **Bottom line:** Launch moves from Mar 3 → Mar 17 (two weeks). Recommend we hold rather than ship the known payment-edge defect.
> **Why:** two load-bearing reasons, in business terms. **Confirmed vs. still-verifying** separated.
> **Ask:** approve the new date by Fri; comms drafted, owner assigned.
</details>

## Install into Claude Code

```bash
git clone https://github.com/27rdeepak/Professional-AI-Skills.git
cd Professional-AI-Skills

# Available in every project (installs into ~/.claude/skills)
python3 scripts/install_skills.py --global

# Or ship them with a specific repo (creates ./.claude/skills, travels with the clone)
python3 scripts/install_skills.py
```

Then invoke any skill by name, e.g. `/risk-analysis` or `/threat-modeling`. Working inside a clone of this repo, the bundled `.claude/skills/` mount means the skills are already available with no install step.

## Browse the catalog

A searchable catalog of all 112 skills is generated to `docs/index.html`:

```bash
python3 scripts/build_site.py
```

Published via GitHub Pages at **https://27rdeepak.github.io/Professional-AI-Skills/** (enable once under Settings → Pages → Deploy from a branch → `main` → `/docs`).

## Quick start (any assistant)

1. Browse the [catalog](docs/catalog.md).
2. Copy a skill folder into a supported skills directory, or upload its `SKILL.md` as project knowledge.
3. Invoke it: `Use $risk-analysis to assess this proposal.`
4. Combine only the few skills a task needs.

See [platform guidance](platform/README.md).

## What's inside

112 skills across 12 domains:

| Domain | Examples |
|---|---|
| Core reasoning | critical-thinking, decision-analysis, premortem-analysis, root-cause-analysis |
| Business & strategy | business-case-building, financial-impact-analysis, swot-analysis, pricing-strategy |
| Communication | executive-writer, executive-brief, board-communication, risk-communication |
| Cybersecurity | threat-modeling, vulnerability-management, incident-response, zero-trust-architecture |
| Enterprise IT | cloud-governance, vendor-management, disaster-recovery-planning |
| Microsoft 365 | entra-id-governance, defender-operations, purview-compliance |
| Leadership | change-leadership, difficult-conversations, delegation-design |
| Research | research-synthesizer, evidence-validation, forecasting, source-triage |
| Software engineering | code-review, architecture-review, debugging-analysis, test-strategy |
| Productivity | prioritization, time-management, decision-journal |
| AI product | agent-design, rag-design, evaluation-design, prompt-optimization |

Full list in the [catalog](docs/catalog.md).

## Quality gates

```bash
python3 scripts/validate_repository.py   # structure and frontmatter
python3 scripts/run_checks.py            # per-skill quality contract + mirror sync
```

`run_checks.py` enforces that every skill has a concrete trigger, a real multi-step workflow, a bounded output, a worked example, named failure modes, resolving cross-links, and that the committed `.claude/skills/` mount matches the canonical `skills/` source. Both run in CI on every push.

## Repository map

- `skills/` — reusable capability folders (canonical source)
- `.claude/skills/` — flattened Claude Code mount (generated; kept in sync by CI)
- `frameworks/` — shared analytical methods
- `templates/` — output structures
- `playbooks/` — multi-stage workflows
- `personas/` — legitimate stakeholder lenses
- `evaluations/` — rubrics and executable forward tests
- `docs/` — specification, style guide, and catalog

## Contributing

Read the [skill specification](docs/skill-specification.md), [style guide](docs/style-guide.md), and [contribution guide](CONTRIBUTING.md). Every PR runs the validator and the quality checks, so contributions stay at the bar.

## License

[MIT](LICENSE) — free for everyone to use, adapt, and share.
