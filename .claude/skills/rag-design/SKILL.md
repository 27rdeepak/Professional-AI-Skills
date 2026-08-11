---
name: rag-design
description: Define retrieval needs, sources, chunking, ranking, citations, and freshness for a RAG system. Use when designing or debugging retrieval-augmented generation, choosing chunking or ranking strategy, adding citations or freshness controls, or diagnosing why answers miss or hallucinate context.
---

# RAG Design

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the questions the system must answer and the freshness they need.
2. Identify sources, their authority, and update frequency.
3. Design chunking and indexing for the query patterns.
4. Choose retrieval and ranking, and set citation requirements.
5. Define freshness, deduplication, and stale-content handling.
6. Recommend evaluation for retrieval quality and answer faithfulness.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **RAG design and retrieval plan** with:

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

- **Retrieval blind spot:** most RAG failures are retrieval, not generation — measure it.
- **Citation theater:** a citation that does not support the sentence is worse than none.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $rag-design to design retrieval for a support assistant over a product knowledge base."

Define the question types and freshness needs, inventory the KB sources, chunk around how questions are actually asked, set ranking and mandatory citations, handle stale articles, and recommend separate evals for retrieval hit-rate and answer faithfulness.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `evidence-validation` for citation quality and `evaluation-design` for the eval.
