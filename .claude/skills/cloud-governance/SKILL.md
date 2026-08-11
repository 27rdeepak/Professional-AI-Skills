---
name: cloud-governance
description: Define cloud guardrails, account structure, policy, and exception handling, and check whether controls are preventative, detective, and recoverable. Use when reviewing a cloud landing zone or governance model, addressing cost, identity, logging, or ownership drift, setting guardrails for multi-account estates, or preparing a cloud governance or audit review.
---

# Cloud Governance

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Establish the environment: accounts or subscriptions, ownership, and the governance objective.
2. Review guardrails and policy — where they prevent, where they detect, and where they enable recovery.
3. Find drift in cost, identity, logging, and ownership.
4. Separate preventative controls from detective and recoverable ones, and flag the gaps.
5. Assess exception handling and review cadence.
6. Recommend guardrails, review cadence, and escalation paths.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **cloud governance assessment** with:

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

- **Detective-only posture:** detection without prevention lets misconfiguration ship first.
- **Ungoverned exceptions:** an exception with no expiry becomes the standard.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** separate observed configuration from assumed policy.
- **Ownership gaps:** an account with no owner drifts on cost and security.

## Example

**Request:** "Use $cloud-governance to review a fast-growing AWS estate with 60 accounts and rising costs."

Establish the account structure and ownership, then check preventative guardrails such as SCPs and tagging policy against detective-only controls. Surface cost and logging drift, flag the ungoverned exceptions that have quietly become defaults, and recommend guardrails with a review cadence and escalation path.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `security-architecture-review` for control design, `enterprise-asset-inventory` for coverage, and `financial-impact-analysis` for the cost picture.
