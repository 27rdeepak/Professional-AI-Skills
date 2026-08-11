---
name: kpi-design
description: Define what to measure, why it matters, how it is calculated, and what good looks like. Use when designing KPIs or a metrics framework, fixing a metric that drives the wrong behavior, defining 'good' for a team or product, or trimming a bloated dashboard to the few metrics that matter.
---

# KPI Design

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the outcome the metric should drive and for whom.
2. Choose the few metrics that reflect that outcome, not activity.
3. Specify each metric's formula, source, and cadence precisely.
4. Define what 'good' is: target, threshold, and direction.
5. Test each metric for gaming and perverse incentives.
6. Recommend the metric set and what to retire.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **KPI definition set** with:

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

- **Activity as outcome:** measure the result, not the busywork that may not produce it.
- **Gameable metric:** a metric that can be hit without the outcome will be.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $kpi-design to design KPIs for a support team beyond ticket volume."

Define the outcome (resolved customers, not closed tickets), choose metrics like first-contact resolution and recurrence, specify each formula and source, set targets, test for gaming (closing-and-reopening), and recommend retiring raw ticket count as a headline metric.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `decision-analysis` for weighting and `quality-review` to check the definitions.
