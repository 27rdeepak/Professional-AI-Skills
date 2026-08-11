---
name: incident-postmortem
description: Reconstruct timeline, cause chain, impact, detection, response, and recovery. Use when writing a blameless postmortem after an incident, analyzing how a failure unfolded and was handled, extracting preventive actions, or reviewing detection and response gaps.
---

# Incident Postmortem

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Reconstruct the timeline from detection to recovery.
2. Establish the cause chain, not a single culprit.
3. Quantify impact on users and the business.
4. Assess detection, response, and recovery for gaps.
5. Separate contributing factors from the trigger.
6. Recommend preventive and detective actions with owners.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **blameless postmortem** with:

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

- **Blame termination:** 'human error' is a starting point — ask what let it cause harm.
- **Single root cause:** most incidents are a chain; address the contributing factors too.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $incident-postmortem to write a postmortem for a two-hour outage."

Reconstruct the timeline, build the cause chain (a config change plus a missing canary), quantify the customer impact, assess why detection lagged, separate the trigger from the contributing gaps, and recommend the canary and alerting actions with owners.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `root-cause-analysis` for the cause chain and `risk-analysis` for residual exposure.
