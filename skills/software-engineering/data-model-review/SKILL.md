---
name: data-model-review
description: Assess entities, relationships, constraints, lifecycle, and usage patterns. Use when reviewing or designing a data model or schema, diagnosing integrity or performance issues, planning a schema change, or evaluating whether a model fits its access patterns.
---

# Data Model Review

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the domain and the access patterns the model must serve.
2. Map entities, relationships, keys, and constraints.
3. Check integrity: what the schema does and does not enforce.
4. Assess the model against real query and write patterns.
5. Evaluate lifecycle, history, and migration implications.
6. Recommend changes ranked by integrity and performance risk.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **data-model review** with:

1. Bottom line
2. Evidence and analysis
3. Risks, uncertainties, and alternatives
4. Recommendation or next test
5. Actions, owners, and timing when known

Adapt to the requested format. Use tables only when they improve comparison.

## Quality check

- Answer the actual decision or objective.
- Support, qualify, or label every material claim.
- Preserve units, periods, baselines, and source context.
- Make risks and alternatives specific.
- Ensure the recommendation follows from the analysis.
- Keep the result concise enough for its audience.

## Failure modes

- **Normalization dogma:** fit the model to access patterns, not to a rulebook.
- **Silent integrity gaps:** enforce invariants in the schema, not only in application code.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $data-model-review to review a schema before it goes to production."

Define the access patterns, map entities and keys, flag the missing foreign-key constraint that lets orphans form, assess it against the hot read path, evaluate the migration cost, and recommend the constraint and index changes ranked by integrity risk.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `architecture-review` for the system and `quality-review` for the change.
