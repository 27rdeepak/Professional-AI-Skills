---
name: agent-design
description: Assess an AI agent's goals, tools, autonomy, memory, guardrails, and handoffs. Use when designing or reviewing an autonomous or tool-using agent, deciding how much autonomy to grant, adding guardrails or human handoffs, or debugging why an agent loops, over-acts, or loses context.
---

# Agent Design

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the agent's job, success criteria, and the outcomes it must never produce.
2. Specify the tools and actions it can take, and the scope limit on each.
3. Set the autonomy level and the decision points that require human approval or handoff.
4. Design memory and context: what it retains, retrieves, and forgets, and why.
5. Add guardrails — input validation, output checks, rate and cost limits, and stop conditions.
6. Define evaluation, monitoring, and the fallback when the agent is uncertain or fails.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **agent design and guardrail spec** with:

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

- **Autonomy overreach:** grant the least autonomy that does the job and escalate the rest.
- **Guardrail afterthought:** design stop conditions and limits with the capability, not after.
- **Context hoarding:** unbounded memory degrades reasoning and leaks state.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary between evidence and recommendation.

## Example

**Request:** "Use $agent-design to design a support agent that can issue refunds up to a limit."

Define the job and the never-do outcomes (no refund above policy), scope the refund tool with a hard cap, require human approval above it, bound memory to the current ticket, add output checks and a cost limit, and define the fallback when confidence is low.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Combine with `evaluation-design` to test it, `workflow-automation` for the surrounding process, and `risk-analysis` for failure impact.
