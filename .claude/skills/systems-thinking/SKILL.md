---
name: systems-thinking
description: Analyze feedback loops, dependencies, incentives, delays, and unintended consequences across a system. Use when a fix keeps failing or creating new problems elsewhere, when local optimization is hurting the whole, or when you need to find leverage points before intervening in an organization, process, or product.
---

# Systems Thinking

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Set the system boundary, key actors, stocks, flows, and the objective.
2. Map reinforcing and balancing loops, and mark the delays between cause and effect.
3. Identify where local optimization degrades the whole.
4. Locate leverage points, ranked by impact and feasibility.
5. Trace the likely second- and third-order effects of intervening at each point.
6. Recommend where to act and the signals that would show it working or backfiring.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **system map and leverage-point brief** with:

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

- **Loop blindness:** account for delays — effects that lag look like non-effects.
- **Leverage at the wrong level:** parameter tweaks rarely beat structural change.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** label the boundary.
- **Boundary gerrymandering:** draw the boundary to include the actors that actually matter.

## Example

**Request:** "Use $systems-thinking to understand why hiring more support agents didn't reduce ticket backlog."

Map the loop — more agents raise reply speed, which raises expectations, which raises ticket volume, holding backlog steady. Mark the hiring-to-productivity delay, then identify the higher-leverage point: deflecting the root-cause tickets upstream. Name the signal that would confirm the shift and the second-order effect to watch.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `root-cause-analysis` for the failure's origin and `trade-off-analysis` when a leverage point helps one loop but strains another.
