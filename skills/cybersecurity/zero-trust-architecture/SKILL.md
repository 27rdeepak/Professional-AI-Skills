---
name: zero-trust-architecture
description: Evaluate identity, device, network, application, data, and telemetry controls against least-privilege intent, and sequence a pragmatic path to zero trust. Use when assessing zero-trust maturity, planning a segmentation or identity-first initiative, reviewing where implicit trust still bypasses policy, or prioritizing zero-trust investments.
---

# Zero Trust Architecture

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the protect surface: the data, assets, applications, and services that matter most.
2. Assess each pillar — identity, device, network, application, data, telemetry — against least-privilege intent.
3. Find where implicit trust still bypasses policy: flat networks, standing admin, unmanaged devices.
4. Prioritize control layering by risk reduction and feasibility.
5. Sequence a migration that preserves operations and avoids big-bang cutovers.
6. Recommend guardrails, success metrics, and the first concrete increment.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **zero-trust assessment and roadmap** with:

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

- **Product-as-strategy:** zero trust is an architecture, not a tool purchase.
- **Big-bang risk:** sequence increments; a flip-the-switch cutover breaks operations.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** separate enforced policy from aspirational policy.
- **Protect-surface drift:** anchor every control to a defined asset, not the whole network.

## Example

**Request:** "Use $zero-trust-architecture to assess a company still on a flat corporate network with VPN access."

Define the protect surface, score each pillar against least-privilege intent, and flag the flat network and standing VPN trust as the top gaps. Sequence identity-first controls and segmentation as staged increments, each with a success metric and a guardrail so operations keep running through the migration.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Build on `security-architecture-review` for design detail and `threat-modeling` for the attack paths segmentation should close.
