---
name: incident-response
description: Classify a security event's scope, severity, and containment needs, then drive it through detection, containment, eradication, recovery, and lessons learned with evidence preserved. Use when triaging a suspected breach or active incident, running an incident bridge, deciding containment and escalation, or writing the post-incident review.
---

# Incident Response

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Establish the facts: what was observed, when, on which assets, and the current status.
2. Classify scope and severity, and decide whether to formally declare an incident.
3. Contain to stop spread while preserving forensic evidence; log every action with a timestamp and owner.
4. Eradicate the root cause and verify the threat and any persistence are removed.
5. Recover services with validation and heightened monitoring.
6. Capture the timeline, decisions, and lessons learned as concrete, owned follow-ups.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to an **incident brief and action log** with:

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

- **Evidence destruction:** contain without wiping the forensic trail.
- **Premature all-clear:** confirm eradication before declaring recovery.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** separate what is confirmed from what is suspected.
- **Silent timeline:** record decisions, owners, and timestamps as you go, not after.

## Example

**Request:** "Use $incident-response to triage a suspected credential-compromise alert on a production admin account."

Establish the facts and current status, classify severity (privileged access makes it high), and contain by disabling the account and rotating keys while preserving the auth logs. Verify no persistence or lateral movement, recover under heightened monitoring, and log the timeline with owned follow-ups such as enforcing MFA on that account class.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Use `threat-modeling` to anticipate the abuse paths, `root-cause-analysis` for the underlying cause, and `executive-writer` for the leadership update.
