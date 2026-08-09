---
name: architecture-review
description: Assess components, boundaries, responsibilities, dependencies, and failure modes. Use when reviewing a system or service architecture, evaluating a design before build, diagnosing coupling or scaling problems, or preparing an architecture decision record.
---

# Architecture Review

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Restate the system's purpose and quality requirements.
2. Map components, boundaries, responsibilities, and dependencies.
3. Assess coupling, cohesion, and where responsibilities blur.
4. Trace the failure modes and how the system degrades.
5. Evaluate scalability, evolvability, and operability against the requirements.
6. Recommend changes ranked by risk and cost.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **architecture review** with:

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

- **Diagram-as-truth:** review the system as built and operated, not the idealized diagram.
- **Gold-plating:** match the architecture to the requirements, not to maximal robustness.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $architecture-review to review a service architecture before a scaling push."

Restate the purpose and the scaling requirement, map the components and dependencies, flag the shared database as a coupling and failure point, trace how it degrades under load, evaluate the evolvability cost, and recommend the decoupling change ranked against the deadline.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `systems-thinking` for dependencies and `risk-analysis` for failure impact.
