---
name: third-party-risk
description: Assess a vendor's access, data exposure, business criticality, control posture, and exit options, separating contractual assurance from operational evidence. Use when onboarding or renewing a supplier, reviewing a vendor's security posture, assessing concentration or fourth-party risk, or deciding whether to accept a vendor's residual risk.
---

# Third-Party Risk

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Map what the vendor accesses: data types, systems, privileges, and the business processes that depend on them.
2. Rate business criticality and the blast radius of a vendor breach or outage.
3. Assess control posture with evidence — attestation scope, test results — not questionnaires or logos alone.
4. Separate contractual assurance (SLAs, clauses) from operational assurance (what is actually running).
5. Identify concentration, fourth-party, and cascade risk.
6. Recommend due diligence, monitoring cadence, contractual controls, and exit feasibility.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **vendor risk assessment** with:

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

- **Certificate theater:** a SOC 2 badge is scope-bound — read the report, not the logo.
- **Exit blindness:** assess how hard it is to leave before you depend on the vendor.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** separate attested controls from assumed ones.
- **Concentration blind spot:** flag where many services share one vendor or sub-processor.

## Example

**Request:** "Use $third-party-risk to assess a SaaS analytics vendor that will receive customer PII."

Map the PII flow and the vendor's privileges, rate criticality, and test the control claims against the actual scope of their SOC 2 report. Separate contract terms from operating reality, flag concentration and the cost of exit, and recommend monitoring plus specific contractual data-handling controls.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `security-architecture-review` for the integration design, `risk-analysis` to track residual exposure, and `commercial-negotiation` for the contract terms.
