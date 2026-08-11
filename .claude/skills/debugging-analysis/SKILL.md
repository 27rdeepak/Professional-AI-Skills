---
name: debugging-analysis
description: Reconstruct symptom, reproduction path, expected state, and observed state. Use when diagnosing a bug or unexpected behavior, isolating a hard-to-reproduce failure, structuring a debugging investigation, or narrowing a fault to its cause.
---

# Debugging Analysis

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Reconstruct the symptom, expected state, and observed state.
2. Establish a reliable reproduction or the closest available.
3. Form hypotheses and rank them by likelihood and cheapness to test.
4. Narrow the fault with discriminating tests, not guesses.
5. Confirm the cause and the exact conditions that trigger it.
6. Recommend the fix and a test that would catch a regression.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **debugging analysis** with:

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

- **Guess-and-patch:** narrow with discriminating tests, do not change code hoping it helps.
- **Symptom fix:** confirm the cause; a masked symptom recurs.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $debugging-analysis to diagnose an intermittent 500 error under load."

Reconstruct the symptom and expected state, find the load condition that reproduces it, rank hypotheses (connection-pool exhaustion first), run a discriminating test on pool metrics, confirm the exhaustion and its trigger, and recommend the fix with a load test that would catch the regression.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `root-cause-analysis` for recurring faults and `incident-postmortem` after an outage.
