---
name: ai-governance
description: Define policy, review points, risk tiers, approvals, and ownership for AI usage. Use when standing up AI governance, classifying AI use cases by risk, deciding what needs human approval, or responding to a regulatory or internal-audit requirement for AI oversight.
---

# AI Governance

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Inventory AI use cases and classify each by risk tier and impact.
2. Define the policy: permitted uses, prohibited uses, and required disclosures.
3. Set review and approval gates proportionate to each risk tier.
4. Assign ownership and accountability for each control.
5. Define monitoring, incident handling, and the audit evidence to retain.
6. Recommend the rollout and the review cadence.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **AI governance policy and control map** with:

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

- **One-tier-fits-all:** match control weight to risk; do not gate low-risk uses like high-risk ones.
- **Ownerless policy:** a control with no owner is not enforced.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $ai-governance to set up oversight for teams adopting generative AI tools."

Inventory and tier the use cases (customer-facing versus internal drafting), write permitted and prohibited uses, gate high-risk uses behind human approval, assign control owners, and define the audit evidence and review cadence.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `risk-analysis` for use-case exposure and `human-in-the-loop-design` for the oversight controls.
