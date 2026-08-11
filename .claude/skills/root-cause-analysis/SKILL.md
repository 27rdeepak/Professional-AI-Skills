---
name: root-cause-analysis
description: Diagnose a recurring or high-impact failure by building an evidence-backed causal chain and proposing corrective and preventive actions. Use when a failure keeps recurring or symptom-level fixes have not held — incident postmortems, repeated defects, or process breakdowns that need a "why does this keep happening?" diagnosis.
---

# Root Cause Analysis

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the failure precisely: what happened, the expected state, scope, and timeline.
2. Assemble the evidence and reconstruct the sequence of events.
3. Build the causal chain, testing each link against the evidence — would removing it have prevented the failure?
4. Separate root causes from contributors, triggers, and symptoms.
5. Distinguish technical causes from process and systemic ones.
6. Propose corrective actions for this instance and preventive actions against recurrence, each with a verification and owner.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **causal analysis and CAPA plan** with:

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

- **Single-cause bias:** most failures are a chain, not one culprit.
- **Blame termination:** "human error" is a symptom — ask what let it cause harm.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and hypothesis.
- **Fix without verification:** every corrective action needs a way to confirm it worked.

## Example

**Request:** "Use $root-cause-analysis to diagnose why the same checkout error keeps recurring after each fix."

Define the error and its conditions, reconstruct the timeline, and test the causal chain — the prior fixes addressed the symptom, not the shared config path they all touched. Separate the root cause (no integration test guarding that path) from triggers, and propose a preventive action with a verification test that would fail if the path regresses.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Feed the findings into `knowledge-distillation` for reusable prevention rules, and pair with `systems-thinking` when the causes are structural rather than local.
