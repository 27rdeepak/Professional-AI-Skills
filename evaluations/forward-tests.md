# Forward Tests

## Purpose

Check whether each skill is distinct, reusable, and decision-useful — not just structurally valid.

## Executable runner

`scripts/run_checks.py` turns these checks into deterministic, per-skill assertions that run in CI (no model required). It fails the build if any skill regresses.

```bash
python3 scripts/run_checks.py
```

## Checks enforced per skill

- **Correct trigger** — concrete `Use when` language; no generic boilerplate or pipe-stuffed description.
- **Clear workflow** — a real multi-step procedure (>= 3 steps), not a one-line `Combine with ...` stub.
- **Bounded output** — a named default artifact or an explicit output contract.
- **Representative example** — a worked `## Example`, not a placeholder.
- **Safe uncertainty handling** — a named `## Failure modes` (or `## Failure recovery`) section.
- **Resolving cross-links** — every related-skills reference points to a real skill; no self-reference.
- **Agent metadata** — `agents/openai.yaml` exists and references `$skill-name`.

## Global check

- Every skill named in `tests/regression-suite.md` exists in the library.

## Runtime behaviors (not automated)

The prompt-and-expected pairs in `tests/regression-suite.md` describe model-dependent output quality (e.g. "mentions disagreement explicitly"). These require a model to evaluate and are exercised manually or in a separate harness.
