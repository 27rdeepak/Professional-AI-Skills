---
name: purview-compliance
description: Design and assess Microsoft Purview governance across data classification, sensitivity labels, data loss prevention, retention, records, eDiscovery, insider risk, audit, and evidence. Use when building a Microsoft 365 compliance program, preparing an audit or investigation, reducing oversharing, implementing information protection, or reviewing Purview policy scope and operational effectiveness.
---

# Purview Compliance

## Operating standard

Start with legal, regulatory, contractual, and business requirements; do not deploy controls merely because a feature exists. Separate policy simulation, enforcement, coverage, user behavior, alert handling, and demonstrated effectiveness.

## Inputs

Obtain obligations, data classes, business processes, locations and workloads, licensing, label taxonomy, retention schedule, DLP policies, record requirements, investigation processes, alert volumes, exceptions, administrative roles, and evidence needs.

## Workflow

1. Translate obligations and business needs into explicit information-handling outcomes.
2. Map sensitive data types, repositories, owners, flows, sharing patterns, and lifecycle stages.
3. Assess classification quality, label usability, default behavior, inheritance, and user override.
4. Review DLP scope, rule logic, thresholds, simulation results, exceptions, and incident workflow.
5. Evaluate retention and deletion against record categories, holds, conflicts, and system coverage.
6. Assess audit, eDiscovery, insider-risk, and investigation readiness with privacy safeguards.
7. Test role separation, change governance, monitoring, tuning, and user support.
8. Sequence policy pilots, enforcement, training, evidence collection, and periodic review.

## Decision rules

- Do not enforce broad policies until false positives and business workarounds are measured.
- Resolve conflicts among retention, deletion, legal hold, and backup behavior explicitly.
- Treat labels as a user experience and operating model, not just metadata.
- Require an accountable process for alerts, exceptions, overrides, and policy tuning.
- Validate workload and location coverage against actual licensing and configuration.

## Output

Provide:

1. Compliance outcomes and scope
2. Data, workload, and lifecycle map
3. Classification, DLP, retention, and investigation findings
4. Policy gaps and operational bottlenecks
5. Phased implementation or remediation plan
6. Testing, evidence, and effectiveness metrics
7. Ownership, privacy safeguards, and decisions required

## Quality check

- Recommendations trace to a requirement or material data risk.
- Policy scope, exclusions, and licensing assumptions are explicit.
- Enforcement plans include simulation, pilot, communication, and rollback.
- Operational ownership and investigation capacity are realistic.
- Effectiveness is measured beyond policy count.

## Failure recovery

If legal requirements or retention schedules are unclear, identify the decision points for counsel or records owners and avoid irreversible deletion recommendations.

## Example

**Request:** “Create a Purview roadmap for sensitive customer and financial information across SharePoint, Teams, Exchange, and endpoints.”

Map data use and obligations, then phase labels, DLP, retention, investigation, and operating governance.

## Evaluation

A strong result is requirement-led, workload-specific, usable, privacy-aware, and measurable.

## Related skills

Use `sharepoint-governance` for site controls, `endpoint-management` for device enforcement, and `compliance-readiness` for assurance evidence.
