---
name: test-strategy
description: Define what must be true, what can fail, and which tests prove it. Use when designing a test strategy for a feature or system, deciding what and how to test under time limits, closing coverage gaps by risk, or justifying a testing approach.
---

# Test Strategy

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define what must be true for the feature to be correct.
2. Identify what can fail and the consequence of each failure.
3. Choose test types and levels matched to those risks.
4. Prioritize coverage by risk, not uniform breadth.
5. Define the automation, data, and environments needed.
6. Recommend the strategy and the gaps consciously accepted.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **test strategy** with:

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

- **Coverage for its own sake:** target the risky paths, not a percentage number.
- **Testing the trivial:** spend effort where failure hurts, not on getters and glue.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $test-strategy to design a test strategy for a new checkout flow."

Define correctness (no double-charge, correct totals), identify the high-consequence failures, choose unit tests for pricing and end-to-end for the payment path, prioritize the money paths, define the test data and sandbox, and recommend the strategy with the accepted gap on rare currencies.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `quality-review` for the deliverable and `risk-analysis` to weigh accepted gaps.
