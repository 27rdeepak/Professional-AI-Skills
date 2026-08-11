---
name: premortem-analysis
description: Imagine a plan has already failed and work backward to the plausible causes, then convert each into a preventive control, warning signal, and owner. Use when a plan is about to be committed — ahead of a launch, migration, reorg, investment, or major project — especially when confidence is high, the plan is hard to reverse, or dissent has gone quiet.
---

# Premortem Analysis

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Fix the decision and a specific future date at which it has already failed.
2. Independently generate failure narratives across major domains: technical, adoption, market, execution, financial, and external.
3. For each, state the mechanism — the concrete chain of events that produced the failure, not just the label.
4. Rank by likelihood, impact, detectability, and time-to-harm.
5. Assign a preventive control, an early-warning indicator, a contingency, and an owner to the top failures.
6. Name the single failure that, if unaddressed, most threatens the objective.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **ranked failure-mode register** with:

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

- **Optimism capture:** generate failures before mitigations, or the list stays shallow.
- **Undetectable risks:** prioritize the failures you cannot currently see coming.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary.
- **Label without mechanism:** name the causal chain, not just "adoption risk."

## Example

**Request:** "Use $premortem-analysis on a planned Q4 platform migration the team is confident about."

Assume it failed by year-end. Generate failure narratives — data-integrity loss at cutover, adoption stall, an unmigrated dependency, an untested rollback — and state the mechanism for each. Rank by impact and detectability, then assign every top failure a preventive control, a warning signal, and an owner, flagging the untested rollback as the top undetected risk.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Combine with `risk-analysis` to quantify and track the register, `decision-analysis` when the premortem should change a go/no-go, and `quality-review` on the resulting mitigation plan.
