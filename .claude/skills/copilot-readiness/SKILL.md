---
name: copilot-readiness
description: Assess organizational and technical readiness for Microsoft 365 Copilot across business use cases, licensing, identity, permissions, information hygiene, data protection, adoption, support, measurement, and governance. Use when planning a Copilot pilot or rollout, evaluating oversharing risk, choosing user cohorts, building an adoption plan, or deciding whether deployment should proceed.
---

# Copilot Readiness

## Operating standard

Evaluate whether Copilot will amplify useful work or amplify existing access and information problems. Do not treat licensing, enthusiasm, or a successful demo as proof of readiness or value.

## Inputs

Obtain priority use cases, user cohorts, licensing, tenant and identity posture, SharePoint and Teams governance, permission and sharing patterns, data classification, retention and DLP controls, endpoint posture, support model, training capacity, and success measures.

## Workflow

1. Define measurable work outcomes and select use cases with suitable data and repeatability.
2. Identify user cohorts, prerequisites, excluded populations, and business owners.
3. Review identity, device, application, and privileged-access prerequisites.
4. Assess information architecture, stale content, oversharing, external access, and permission inheritance.
5. Evaluate sensitive-data controls, retention, audit, investigation, and acceptable-use policy.
6. Design a bounded pilot with baseline measures, control groups where practical, support, and feedback.
7. Define training by role, prompt practices, human verification, and prohibited uses.
8. Establish adoption, value, risk, incident, cost, and support metrics.
9. Set go, pause, expand, or stop criteria for each rollout stage.

## Decision rules

- Prioritize use cases where users can verify outputs and data access is already appropriate.
- Do not use broad content cleanup as a substitute for fixing permission governance.
- Separate activity metrics from time saved, quality improved, or risk reduced.
- Exclude use cases requiring unsupported accuracy, confidentiality, or autonomy.
- Expand only after value and control evidence meet predeclared thresholds.

## Output

Provide:

1. Readiness verdict by dimension
2. Prioritized use cases and excluded uses
3. Identity, data, permission, and compliance gaps
4. Pilot design and cohort rationale
5. Adoption, support, and training plan
6. Value, risk, and cost measurement model
7. Stage gates and executive decisions

## Quality check

- Use cases name a user, task, data source, baseline, and expected outcome.
- Permission and oversharing risks are evidenced, not assumed away.
- Pilot metrics can distinguish novelty from sustained value.
- Training includes verification and escalation behavior.
- Rollout criteria include stop conditions and cost controls.

## Failure recovery

If permission or data-hygiene evidence is unavailable, recommend a bounded discovery pilot or readiness assessment rather than tenant-wide deployment.

## Example

**Request:** “Should we deploy Microsoft 365 Copilot to all 300 employees?”

Return a staged decision based on use-case value, data access, governance, support capacity, measurement, and stop criteria.

## Evaluation

A strong result is outcome-led, permission-aware, measurable, staged, and candid about deployment risk.

## Related skills

Use `entra-id-governance`, `sharepoint-governance`, `purview-compliance`, and `change-leadership` as supporting skills.
