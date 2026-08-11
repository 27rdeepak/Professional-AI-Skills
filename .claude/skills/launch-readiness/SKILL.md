---
name: launch-readiness
description: Assess product quality, support, documentation, messaging, and rollback options before launch. Use when deciding launch go/no-go, running a launch-readiness review, finding gaps that would block release, or preparing a rollback and support plan.
---

# Launch Readiness

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the launch scope and the bar for go.
2. Assess product quality, support readiness, documentation, and messaging.
3. Verify rollback and incident response are in place and tested.
4. Separate must-fix blockers from acceptable-with-mitigation gaps.
5. Confirm ownership for launch-day decisions.
6. Recommend go, go-with-conditions, or hold with the gating items.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **launch-readiness assessment and go/no-go** with:

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

- **Feature-complete is not launch-ready:** support, docs, and rollback gate the launch too.
- **Untested rollback:** a rollback that has never run is not a safety net.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $launch-readiness to decide go/no-go for a payments feature shipping Friday."

Set the go bar, assess quality and support readiness, confirm the rollback is tested, separate the one must-fix blocker from acceptable gaps, name the launch-day decision owner, and give a go-with-conditions verdict.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `release-management` for the rollout and `premortem-analysis` for what could fail.
