---
name: evaluation-design
description: Define success criteria, datasets, tests, rubrics, and failure thresholds for a system. Use when building an evaluation for an AI feature or model, deciding what 'good enough to ship' means, designing test sets and rubrics, or diagnosing why a system passes offline but fails in production.
---

# Evaluation Design

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define what the system must do and what 'good enough to ship' means.
2. Choose metrics tied to the real user outcome, not proxy convenience.
3. Build datasets: representative, edge, and adversarial cases.
4. Write rubrics and pass thresholds per metric.
5. Separate offline evaluation from production monitoring.
6. Define what a failing evaluation triggers.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **evaluation plan and rubric** with:

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

- **Proxy metric drift:** optimize the outcome, not a metric that diverges from it.
- **Happy-path only:** include edge and adversarial cases, or the eval lies.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $evaluation-design to build an eval for a summarization feature before launch."

Define ship criteria, pick metrics tied to reader usefulness, assemble representative and adversarial documents, write a rubric with thresholds, separate offline scores from production monitoring, and state what a fail blocks.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `quality-review` for the rubric and `evidence-validation` for factuality checks.
