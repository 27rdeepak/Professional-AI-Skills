---
name: prompt-optimization
description: Improve a prompt's clarity, constraints, examples, and output shape without overfitting. Use when a prompt gives inconsistent or wrong-format output, when tightening an LLM instruction, when adding examples or guardrails, or when iterating on a prompt that fails on edge cases.
---

# Prompt Optimization

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the task, the desired output shape, and the failure the prompt shows.
2. Diagnose whether the issue is clarity, constraints, examples, or format.
3. Tighten the instructions and make the output contract explicit.
4. Add targeted examples that cover the failing cases without overfitting.
5. Test against held-out and edge inputs.
6. Recommend the revision and what to monitor.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **improved prompt and rationale** with:

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

- **Overfitting to examples:** examples should generalize, not memorize the test cases.
- **Instruction bloat:** more words can dilute; cut what does not change the output.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $prompt-optimization to fix a prompt that sometimes returns prose instead of JSON."

Define the required JSON contract, diagnose the missing format constraint, make the schema explicit, add one example covering the failing case, test on held-out inputs, and recommend the revision with a check for format regressions.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `evaluation-design` to measure it and `quality-review` for output checks.
