---
name: first-principles-analysis
description: Decompose a problem to its fundamental constraints and rebuild options without inherited assumptions. Use when "that's how it's always been done" is blocking progress, when cost or architecture seems fixed by convention rather than physics or economics, or when you need to test whether a long-held requirement is truly a constraint.
---

# First Principles Analysis

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the desired outcome independently of the current solution.
2. List every stated requirement and constraint.
3. Classify each as a fundamental constraint — physics, law, economics, contract — or a convention that can be questioned.
4. Break the remaining claims into falsifiable assumptions and test the biggest ones.
5. Rebuild candidate options from only the validated primitives.
6. Compare the reconstructed options to the status quo and name what the convention was costing.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **constraint and assumption ledger** with:

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

- **False bedrock:** do not accept a convention as a law without testing it.
- **Rebuild theater:** reconstruction must yield a materially different option, or say so.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary.
- **Constraint denial:** do not wish away a real physical, legal, or economic limit.

## Example

**Request:** "Use $first-principles-analysis to question why our customer onboarding takes six weeks."

Define the real outcome — customer live and transacting — and separate true constraints (a regulatory KYC step) from conventions (sequential handoffs, weekly batch jobs). Test the assumption that steps must run in sequence, then rebuild a parallelized path that preserves the KYC dependency and name the weeks the convention was costing.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `problem-framing` to fix the outcome, `systems-thinking` for the dependencies, and `trade-off-analysis` when the rebuilt option sacrifices something.
