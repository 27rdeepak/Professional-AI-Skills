---
name: threat-modeling
description: Define assets, trust boundaries, entry points, actors, and abuse cases for a system, then map attack paths to controls and residual risk. Use when designing or changing a system, before a security design review, when adding a new integration or data flow, or to prioritize security work by realistic attack paths.
---

# Threat Modeling

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the assets worth protecting and the unacceptable outcomes.
2. Draw components, data flows, trust boundaries, and entry points.
3. Enumerate actors and their capabilities, from external attacker to malicious insider.
4. Derive abuse cases per entry point (e.g. via STRIDE) and trace plausible attack paths.
5. Map existing controls to each path and expose the gaps.
6. Translate the top threats into business consequence and recommend mitigations, tests, or accepted residual risk.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **threat model and prioritized mitigations** with:

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

- **Checklist substitution:** model this system's flows, not a generic threat list.
- **Severity by label:** rank by attack-path feasibility and consequence, not CVSS alone.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** separate observed design from assumed behavior.
- **Boundary omission:** every trust boundary crossing is a candidate attack surface.

## Example

**Request:** "Use $threat-modeling on a new webhook endpoint that lets partners push order updates."

Define the asset (order integrity), draw the flow and the trust boundary at the partner edge, and enumerate actors — a spoofed partner, a replayed request. Derive abuse cases, map the current auth and validation controls to each path, and recommend signature verification and replay protection, each with a test that would fail if the control regresses.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Feed into `security-architecture-review` for the full design and `vulnerability-management` to prioritize the resulting findings.
