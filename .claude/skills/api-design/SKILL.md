---
name: api-design
description: Define the purpose, users, verbs, objects, constraints, error handling, and compatibility rules of an API. Use when designing a new API or endpoint, reviewing an API for consistency and compatibility, planning versioning and error semantics, or fixing an API that is hard to consume.
---

# API Design

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the API's purpose, consumers, and the tasks it must support.
2. Model the resources or verbs and their relationships.
3. Design consistent naming, pagination, and error semantics.
4. Specify compatibility and versioning rules.
5. Define auth, rate limits, and idempotency for unsafe operations.
6. Recommend the contract and the review before it ships.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **API design and contract** with:

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

- **Implementation leakage:** design for the consumer's task, not your internal model.
- **Breaking-change creep:** version deliberately; do not silently break existing clients.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $api-design to design an endpoint for partners to submit and query orders."

Define the partner tasks, model the order resource, design consistent naming and error codes, set the versioning rule, make submission idempotent with a client key, add auth and rate limits, and recommend the contract for review before release.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `architecture-review` for the surrounding system and `quality-review` for the contract.
