---
name: endpoint-management
description: Review device enrollment, configuration, patch posture, compliance, and support coverage, separating policy gaps from deployment gaps and user exceptions. Use when assessing endpoint or MDM posture, diagnosing patch or compliance drift, standardizing device baselines, or preparing an endpoint security review.
---

# Endpoint Management

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Establish the device population by platform, ownership, and privilege level.
2. Review enrollment, configuration, patch posture, compliance, and support coverage.
3. Separate policy gaps from deployment gaps and user exceptions.
4. Identify drift by platform, population, and privilege.
5. Assess how exceptions are granted, tracked, and expired.
6. Recommend baselines, enforcement, and exception handling.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to an **endpoint posture and remediation plan** with:

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

- **Enrolled is not compliant:** an enrolled device out of policy is still exposed.
- **Exception sprawl:** untracked exceptions hollow out the baseline.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** separate reported compliance from verified state.
- **Privilege blindness:** weight drift on admin and executive devices highest.

## Example

**Request:** "Use $endpoint-management to assess why 15% of laptops are behind on patches."

Segment the fleet by platform and privilege, then separate a policy gap — no enforced patch deadline — from a deployment gap such as failed update rings. Flag the privileged-user exceptions that carry the most risk, and recommend an enforced baseline with a tracked, expiring exception path.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `intune-management` for the tooling detail and `vulnerability-management` to prioritize the resulting exposure.
