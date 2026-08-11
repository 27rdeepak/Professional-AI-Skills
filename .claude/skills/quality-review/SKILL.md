---
name: quality-review
description: Review a deliverable against explicit acceptance criteria for correctness, completeness, consistency, usability, and risk, then state release readiness. Use when checking whether a document, plan, design, or analysis is good enough to ship — as a release gate, or when someone asks "is this ready to send?"
---

# Quality Review

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Establish or restate acceptance criteria and severity definitions.
2. Check correctness, completeness, consistency, traceability, usability, and compliance against those criteria.
3. Record each finding with a reproducible location, its consequence, and a remedy.
4. Rank findings by severity, not by the order they were found.
5. State a clear verdict: ready, ready with conditions, or not ready.
6. List the must-fix items that gate release.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **severity-ranked review report** with:

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

- **Nit flood:** rank by consequence so blockers are not buried under style notes.
- **Vague findings:** every finding needs a location, a consequence, and a fix.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** separate defects observed from risks inferred.
- **Missing verdict:** always state ready, ready with conditions, or not ready.

## Example

**Request:** "Use $quality-review to assess whether this data-migration plan is release-ready."

Set acceptance criteria — rollback tested, data validated, cutover window agreed — and check the plan against each. Flag that the rollback step lacks a verification test as a must-fix blocker, rank the remaining findings by consequence, and give a "ready with conditions" verdict that lists the gates.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `critical-thinking` to test the deliverable's claims and `risk-analysis` to weigh the residual exposure of shipping with known gaps.
