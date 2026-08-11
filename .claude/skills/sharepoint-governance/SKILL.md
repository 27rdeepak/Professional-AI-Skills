---
name: sharepoint-governance
description: Review SharePoint and OneDrive site lifecycle, permission model, content sprawl, external sharing, and information architecture, separating ownership issues from design issues. Use when assessing SharePoint governance, addressing content sprawl or overexposed sites, reviewing external sharing, or planning retention and cleanup.
---

# SharePoint Governance

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Establish the site estate, lifecycle stages, and ownership.
2. Review the permission model and external sharing exposure.
3. Separate ownership issues from information-architecture design issues.
4. Identify stale, duplicated, or overexposed content patterns.
5. Assess retention and lifecycle controls.
6. Recommend governance, retention, and cleanup actions.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **SharePoint governance plan** with:

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

- **Overexposure blindness:** broad "everyone" permissions are the top data-exposure risk.
- **Ownerless sites:** a site with no owner accumulates sprawl and stale access.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** separate measured sharing data from assumption.
- **Cleanup without governance:** a one-time purge without provisioning rules recurs.

## Example

**Request:** "Use $sharepoint-governance to address sprawl in a tenant with thousands of sites and broad external sharing."

Map lifecycle and ownership, then flag the overexposed and externally shared sites that carry real data-exposure risk. Separate ownership gaps from information-architecture design problems, and recommend retention plus a cleanup and provisioning standard so the sprawl does not simply return.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `purview-compliance` for classification and DLP and `entra-id-governance` for external identity control.
