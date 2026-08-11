---
name: risk-analysis
description: Identify, assess, prioritize, and treat uncertainty against a stated objective, producing a risk register with owners and indicators. Use when a plan, investment, vendor, or change needs its downside made explicit — to build or review a risk register, separating inherent from residual exposure.
---

# Risk Analysis

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Define the objective, scope, time horizon, risk appetite, and the scales for likelihood and impact.
2. Write cause–event–impact statements so each risk is specific and testable.
3. Assess inherent exposure, then residual exposure after existing controls, as separate figures.
4. Prioritize by exposure and by the proximity and velocity of each risk.
5. Assign a treatment — avoid, reduce, transfer, or accept — with an owner, due date, and leading indicator.
6. Note interactions where one risk triggers or amplifies another.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **risk register and treatment plan** with:

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

- **Inherent/residual conflation:** score exposure before and after controls separately.
- **Register rot:** every risk needs an owner and an indicator, or it will not be tracked.
- **Premature certainty:** use ranges or scenarios.
- **Generic advice:** connect treatments to the supplied context.
- **Hidden trade-offs:** name what accepting or transferring a risk sacrifices.

## Example

**Request:** "Use $risk-analysis to assess the risks of outsourcing our data pipeline to a single vendor."

Set the objective and appetite, then write cause–event–impact risks — vendor outage → pipeline halt → reporting gap; concentration → weak exit leverage. Score inherent versus residual exposure after current controls, and assign treatments, owners, and indicators, flagging concentration as the top residual risk with a next test to price the exit path.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `premortem-analysis` to surface failure modes the register missed, `decision-analysis` when the risk should shape the choice, and `third-party-risk` for vendor-specific exposure.
