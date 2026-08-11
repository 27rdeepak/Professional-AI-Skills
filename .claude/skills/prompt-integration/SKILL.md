---
name: prompt-integration
description: Assess how prompts, tools, and instructions interact across a workflow. Use when integrating prompts into a larger system or pipeline, debugging conflicts between instructions and tools, designing multi-step LLM workflows, or reviewing prompt orchestration.
---

# Prompt Integration

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Map how prompts, tools, and instructions interact across the workflow.
2. Identify where instructions conflict or override each other.
3. Check tool contracts and how outputs feed the next step.
4. Assess failure handling between steps and at the boundaries.
5. Test the end-to-end flow on representative and edge inputs.
6. Recommend the fixes and what to monitor.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **prompt-integration review** with:

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

- **Local prompt tuning:** fix the interaction across steps, not one prompt in isolation.
- **Silent handoff failure:** validate the output of one step before the next consumes it.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $prompt-integration to debug a multi-step agent where a later step gets malformed input."

Map the step interactions, find where the extraction prompt's format conflicts with the next step's expectation, check the tool contract at the boundary, add validation on the handoff, test the flow end-to-end, and recommend the schema fix with a boundary check to monitor.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `systems-thinking` for the interactions and `quality-review` for output checks.
