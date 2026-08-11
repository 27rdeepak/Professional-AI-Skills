---
name: enterprise-asset-inventory
description: Map business-critical hardware, software, services, and ownership to reveal coverage gaps and lifecycle risk, separating discovered, registered, and authoritative records. Use when building or auditing an asset inventory or CMDB, finding unsupported or orphaned assets, establishing ownership, or preparing for an audit or security baseline.
---

# Enterprise Asset Inventory

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define scope and what "business-critical" means for this inventory.
2. Reconcile discovered, registered, and authoritative records against each other.
3. Assign ownership and lifecycle stage to each asset class.
4. Identify unsupported, duplicated, or orphaned assets.
5. Quantify coverage gaps and the risk they carry.
6. Recommend cleanup, governance, and ongoing monitoring.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to an **asset inventory and remediation plan** with:

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

- **Single-source trust:** one system is never complete — reconcile across sources.
- **Ownerless assets:** an asset with no owner will not be patched or retired.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** separate discovered fact from registered claim.
- **Lifecycle blindness:** flag end-of-support assets, not just missing ones.

## Example

**Request:** "Use $enterprise-asset-inventory to reconcile a CMDB that disagrees with the endpoint and cloud discovery tools."

Define scope and reconcile the three sources against each other, flagging assets discovered but unregistered and registered but no longer present. Assign owners and lifecycle stages, surface the unsupported and orphaned assets, and recommend a reconciliation cadence that keeps the authoritative record honest.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `endpoint-management` and `cloud-governance` for source data and `vulnerability-management` for the exposure view.
