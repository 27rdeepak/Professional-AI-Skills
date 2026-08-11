---
name: migration-planning
description: Define source, target, cutover approach, dependencies, and rollback path. Use when planning a system, data, or platform migration, designing a safe cutover with rollback, sequencing migration dependencies, or de-risking a large move.
---

# Migration Planning

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the source, target, and what 'done' means.
2. Map dependencies and the order they must move in.
3. Choose a cutover approach and design the rollback path.
4. Plan data validation before, during, and after.
5. Define the go/no-go criteria and the freeze window.
6. Recommend the plan and a rehearsal before the real cutover.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **migration plan with rollback** with:

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

- **Untested rollback:** a rollback that has never been rehearsed is not a safety net.
- **Big-bang cutover:** prefer incremental or reversible cutover where the risk allows.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $migration-planning to plan a database migration for a live service."

Define source, target, and done, map the dependency order, choose a dual-write cutover with a tested rollback, plan validation at each stage, set go/no-go criteria and a freeze window, and recommend a full rehearsal on a copy before the real cutover.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `release-management` for the rollout and `change-leadership` for adoption.
