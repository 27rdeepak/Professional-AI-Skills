---
name: code-review
description: Inspect correctness, readability, maintainability, security, and test coverage. Use when reviewing a pull request or code change, giving structured code feedback, gating a merge on quality, or auditing a module for defects and risk.
---

# Code Review

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Establish what the change is meant to do and its risk.
2. Check correctness against the intent and edge cases.
3. Assess readability, maintainability, and consistency.
4. Check security, error handling, and resource use.
5. Verify tests actually cover the change and its edges.
6. Report findings ranked by severity with a clear verdict.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **code review with ranked findings** with:

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

- **Nit flood:** rank by consequence so real defects are not buried under style notes.
- **Rubber-stamp:** verify the change does what it claims, do not skim for style only.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $code-review to review a pull request that adds a payment retry."

Establish the intent and its risk, check correctness on the retry edge cases (double-charge), assess readability and consistency, check idempotency and error handling, verify the tests cover the retry path, and report findings ranked with an approve-with-changes verdict.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `quality-review` for the broader deliverable and `test-strategy` for coverage.
