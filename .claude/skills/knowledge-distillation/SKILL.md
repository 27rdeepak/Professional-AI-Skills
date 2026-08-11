---
name: knowledge-distillation
description: Extract reusable principles, mental models, and decision rules from dense material so they can be applied later. Use when turning postmortems, research, expert interviews, or documentation into an internal playbook, checklist, or guide — separating durable principles from context-specific detail.
---

# Knowledge Distillation

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the future use case and who will apply the result.
2. Extract concepts, rules, exceptions, worked examples, and the conditions under which each holds.
3. Separate durable principles from local, situation-specific detail.
4. Resolve or flag contradictions across sources.
5. Compress each principle to its trigger, action, and rationale.
6. Organize for retrieval with labels, cross-links, and one worked example per principle.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **reusable concept and principle map** with:

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

- **Context stripping:** keep the conditions under which a principle applies, or it misleads.
- **Summary masquerade:** distillation yields reusable rules, not a shorter recap.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** mark which principles are evidenced versus inferred.
- **Contradiction burial:** surface where sources disagree instead of averaging them away.

## Example

**Request:** "Use $knowledge-distillation to turn three incident postmortems into reusable operating principles."

Extract the recurring failure patterns and the controls that worked, and separate incident-specific detail from durable rules such as "gate config changes behind a canary." Flag where the postmortems disagree, then produce a labeled principle set, each with a trigger, an action, and a worked example.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Feed from `root-cause-analysis` for the source diagnoses, and pair with `quality-review` to check the distilled rules against real cases.
