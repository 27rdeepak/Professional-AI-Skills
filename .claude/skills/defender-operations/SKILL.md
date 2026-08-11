---
name: defender-operations
description: Assess Microsoft Defender alert fidelity, signal coverage, tuning, response ownership, and containment workflow across endpoint, identity, email, and cloud. Use when reviewing a Defender or XDR deployment, diagnosing alert fatigue or missed detections, tuning noisy rules, or clarifying SOC response ownership.
---

# Defender Operations

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Establish which Defender workloads are deployed and what signals they cover.
2. Identify blind spots across endpoint, identity, email, and cloud.
3. Assess alert fidelity: true-positive rate, noise, and duplication.
4. Differentiate noise reduction from true coverage loss when tuning.
5. Review response ownership and the containment workflow.
6. Recommend tuning, coverage fixes, and escalation thresholds.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **Defender operations assessment** with:

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

- **Tuning into blindness:** suppressing noise can silence a real detection — verify first.
- **Ownerless alerts:** a high-fidelity alert no one owns is not a control.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** separate measured alert data from impression.
- **Coverage assumed:** a deployed workload is not the same as covered signal.

## Example

**Request:** "Use $defender-operations to review a SOC drowning in Defender alerts."

Map the deployed workloads and their coverage, measure alert fidelity, and separate genuine noise from real signal before tuning anything. Fix the identity blind spot the noise was hiding, assign response ownership, and set escalation thresholds so high-fidelity alerts reach an owner fast.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `incident-response` for the response workflow and `threat-modeling` for coverage priorities.
