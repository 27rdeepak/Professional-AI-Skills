---
name: intune-management
description: Review Intune enrollment, compliance policies, configuration profiles, app deployment, and remediation, distinguishing device-management policy from operating-system constraint. Use when assessing an Intune deployment, simplifying device baselines, diagnosing compliance or assignment drift, or cleaning up stale profiles and exceptions.
---

# Intune Management

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Establish the enrolled population by platform and ownership.
2. Review compliance policies, configuration profiles, and app deployment.
3. Distinguish device-management policy from operating-system constraint.
4. Surface coverage gaps, conflicting assignments, and stale profiles.
5. Assess how exceptions are assigned and expired.
6. Recommend simplified baselines and enforcement steps.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **device management plan** with:

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

- **Profile sprawl:** overlapping profiles create conflicts that silently fail to apply.
- **Assignment rot:** stale group assignments drift out of the intended scope.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** separate a deliberate policy from an OS limitation.
- **Compliance theater:** a compliance policy no device is assigned to proves nothing.

## Example

**Request:** "Use $intune-management to simplify a tenant with 40 overlapping configuration profiles."

Segment the population, then map the profile conflicts and separate a genuine policy choice from an OS constraint the profile cannot override. Flag the stale assignments that no longer match their target groups, and recommend a consolidated baseline with a clean, documented assignment model.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `endpoint-management` for the broader posture and `entra-id-governance` for compliance-driven conditional access.
