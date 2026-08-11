---
name: entra-id-governance
description: Assess Entra ID tenant structure, identity lifecycle, privileged access, conditional access, and guest control, separating policy intent from effective control. Use when reviewing Entra ID or Azure AD governance, hardening privileged access, auditing conditional access or guest sprawl, or mapping identity risk to business impact.
---

# Entra ID Governance

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Establish tenant structure, identity sources, and the governance objective.
2. Review the identity lifecycle: joiner, mover, leaver, and service accounts.
3. Assess privileged access — standing admin, PIM usage, and role sprawl.
4. Review conditional access and guest or external control for gaps.
5. Separate policy intent from effective, enforced control.
6. Recommend identity governance priorities and guardrails.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to an **identity governance review** with:

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

- **Standing privilege:** permanent admin roles are the top identity risk — time-bound them.
- **Intent is not enforcement:** a conditional-access policy in report-only mode enforces nothing.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** separate configured policy from its effective result.
- **Guest sprawl blind spot:** stale external identities are standing access.

## Example

**Request:** "Use $entra-id-governance to review a tenant with many global admins and open guest access."

Map the tenant and lifecycle, then flag the standing global-admin roles for just-in-time PIM and audit the conditional-access exclusions and guest sprawl. Separate report-only policies from enforced ones, and prioritize the guardrails that most reduce identity risk.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Build on `zero-trust-architecture` for the identity pillar and `incident-response` for compromise scenarios.
