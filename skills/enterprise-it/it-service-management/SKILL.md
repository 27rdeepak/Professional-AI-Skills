---
name: it-service-management
description: Review a service's process, ownership, SLAs, incidents, changes, and dependencies, distinguishing operational process gaps from tool defects. Use when assessing an ITSM process or service desk, diagnosing recurring incidents or queue backlogs, reviewing change or incident management, or improving service operations.
---

# IT Service Management

## Operating standard

Produce decision-useful work, not generic advice. Preserve material facts, quantify where evidence permits, label assumptions, and distinguish observation, inference, and recommendation. Never invent sources, certainty, owners, dates, or measurements.

## Inputs

Obtain the objective, audience, scope, decision deadline, evidence, constraints, prior decisions, and required format. If a missing input could materially reverse the result, state the gap and ask one focused question or proceed with explicit scenarios.

## Workflow

1. Describe the service: scope, ownership, SLAs, and key dependencies.
2. Review incident, change, and request flows and their queue health.
3. Distinguish operational process gaps from tool defects.
4. Surface recurring failures, handoff risk, and SLA breaches with evidence.
5. Trace the highest-impact bottleneck to its cause.
6. Recommend operating improvements and controls.

## Decision rules

- Prefer the smallest sufficient structure.
- Preserve credible dissent and important downside.
- Recommend action only when evidence supports it; otherwise recommend the next discriminating test.
- State what would materially change the conclusion.

## Output

Default to a **service operating review** with:

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

- **Tool-blaming:** most queue pain is process and ownership, not the ITSM tool.
- **Metric vanity:** measure resolution and recurrence, not tickets touched.
- **Framework theater:** omit sections that do not change action.
- **Fact–inference blending:** separate measured queue data from anecdote.
- **Generic process advice:** tie every change to the observed bottleneck.

## Example

**Request:** "Use $it-service-management to review an incident queue that keeps breaching SLA."

Describe the service and its SLAs, review queue health, and separate the process gap — unclear escalation ownership — from any tool limitation. Trace the top breach cause to its origin, and recommend a concrete operating change such as a defined escalation owner and a triage rule, not generic best practice.

## Evaluation

A strong result is accurate, traceable, decision-relevant, proportionate, and actionable. It remains useful if the reader sees only the bottom line, risks, and next action.

## Related skills

Pair with `root-cause-analysis` for recurring incidents and `operating-model-design` for the ownership structure.
