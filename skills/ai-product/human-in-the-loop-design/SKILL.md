---
name: human-in-the-loop-design
description: Design human oversight for AI systems by matching review, approval, intervention, escalation, and learning controls to decision consequence, uncertainty, reversibility, and reviewer capacity. Use when deciding where humans should review AI outputs, designing approval workflows, preventing automation bias, setting confidence thresholds, or evaluating whether an AI-assisted process is safely operable.
---

# Human-in-the-Loop Design

## Operating standard

Use human involvement only where it changes risk or quality. A human click is not meaningful oversight if the reviewer lacks time, context, authority, or a usable alternative. Do not claim that manual review eliminates model risk.

## Inputs

Obtain the task and decision, affected people, consequence of error, reversibility, frequency and volume, model outputs and uncertainty, available ground truth, latency limits, reviewer expertise and capacity, escalation authority, audit needs, and learning goals.

## Workflow

1. Decompose the process into prediction, recommendation, decision, action, and feedback stages.
2. Classify failure modes by consequence, detectability, reversibility, and time to intervene.
3. Determine whether oversight should prevent, detect, correct, authorize, or learn.
4. Choose a control pattern: pre-approval, exception review, sampling, dual control, abstention, escalation, or post-action audit.
5. Define thresholds using calibrated performance and business cost, not arbitrary confidence scores.
6. Design the reviewer interface with relevant context, uncertainty, alternatives, and reason capture.
7. Test reviewer workload, consistency, automation bias, alert fatigue, and override behavior.
8. Define logging, appeal, incident, fallback, and continuous-learning processes.
9. Set launch and expansion gates based on system and reviewer performance.

## Decision rules

- Require stronger intervention for high-consequence, irreversible, rights-affecting, or low-detectability errors.
- Automate low-risk, reversible cases only when monitoring and fallback are reliable.
- Do not route more cases to humans than the operating model can review well.
- Measure reviewer accuracy and disagreement, not just completion time.
- Preserve an appeal or second-look path where decisions materially affect people.

## Output

Provide:

1. Decision and failure-mode map
2. Oversight objectives by process stage
3. Chosen human-control patterns and rationale
4. Threshold and abstention logic
5. Reviewer workflow and information design
6. Capacity, service-level, and escalation model
7. Metrics, audit trail, testing, and expansion gates

## Quality check

- Every human step has purpose, authority, capacity, and success criteria.
- Thresholds are tied to calibrated evidence and consequence.
- Automation bias and reviewer fatigue are explicitly tested.
- Fallback behavior is safe when reviewers or systems are unavailable.
- Metrics cover both AI and human performance.

## Failure recovery

If model calibration or failure data is unavailable, use a conservative pilot with sampling and independent adjudication before setting automation thresholds.

## Example

**Request:** “Design review controls for an AI that prioritizes vulnerabilities and drafts remediation decisions.”

Match oversight to asset criticality, uncertainty, business consequence, exception handling, reviewer capacity, and feedback evidence.

## Evaluation

A strong result makes human oversight purposeful, measurable, operationally sustainable, and proportionate to consequence.

## Related skills

Use `agent-design` for the wider workflow, `evaluation-design` for testing, and `ai-governance` for policy and accountability.
