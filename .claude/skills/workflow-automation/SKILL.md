---
name: workflow-automation
description: Map the trigger, steps, inputs, outputs, failure paths, and human review points of a process. Use when automating a manual workflow, designing automation with safe failure and review points, deciding what to automate versus keep human, or debugging a brittle automated process.
---

# Workflow Automation

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Map the current process: trigger, steps, inputs, outputs, and actors.
2. Identify what is safe to automate versus what needs human judgment.
3. Design the automated flow with explicit inputs, outputs, and idempotency.
4. Define failure paths, retries, and human review or approval points.
5. Add monitoring and an audit trail.
6. Recommend the design and a staged rollout.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **automation design with failure and review points** with:

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

- **Automating the mess:** fix the process before automating it, or you scale the defect.
- **No failure path:** an automation without defined failure handling breaks silently.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $workflow-automation to automate invoice approval routing."

Map the trigger and steps, keep the spend-threshold judgment human, design the routing with idempotent steps, define retries and an approval checkpoint above a limit, add an audit trail, and stage the rollout behind a monitored pilot.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `risk-analysis` for failure impact and `operational-excellence` for the underlying process.
