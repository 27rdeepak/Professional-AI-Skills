---
name: documentation-engineering
description: Structure docs for task completion, discoverability, and maintenance. Use when designing or overhauling documentation, fixing docs users cannot navigate, structuring content around real tasks, or setting up a maintainable docs system.
---

# Documentation Engineering

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Identify the readers and the tasks they need docs to complete.
2. Assess where current docs fail: findability, accuracy, or maintenance.
3. Structure content around tasks, not the code's internal shape.
4. Design for discoverability with clear entry points and search.
5. Plan ownership and a process that keeps docs current.
6. Recommend the structure and the first content to fix.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **documentation plan** with:

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

- **Code-shaped docs:** organize around user tasks, not the module structure.
- **Write-once rot:** docs without an ownership and update process go stale.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $documentation-engineering to overhaul docs users say they cannot navigate."

Identify the readers and their tasks, diagnose that content is accurate but unfindable, restructure around tasks with clear entry points, add search and a getting-started path, assign ownership and an update trigger, and recommend the top task-based page to write first.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `executive-writer` for clarity and `knowledge-distillation` to capture principles.
