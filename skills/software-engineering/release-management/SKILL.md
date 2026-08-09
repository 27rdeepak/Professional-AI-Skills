---
name: release-management
description: Assess scope, readiness, dependencies, rollback, communications, and support coverage. Use when planning a release, running a release-readiness check, coordinating a rollout, or ensuring rollback and support are in place before shipping.
---

# Release Management

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the release scope and the readiness bar.
2. Assess dependencies, sequencing, and coordination needs.
3. Verify rollback, feature flags, and support coverage.
4. Plan communications for internal and external audiences.
5. Set go/no-go criteria and the decision owner.
6. Recommend go, go-with-conditions, or hold with the gating items.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **release plan and readiness check** with:

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

- **Ship-and-pray:** verify rollback and support before release, not after an incident.
- **Silent release:** coordinate communications; a surprise release breaks trust.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $release-management to plan the release of a major version with breaking changes."

Define the scope and readiness bar, sequence the dependent services, verify the rollback and flags, plan customer and support communications for the breaking changes, set go/no-go criteria with an owner, and recommend a go-with-conditions gated on the migration guide.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `risk-analysis` for release risk and `migration-planning` for breaking changes.
