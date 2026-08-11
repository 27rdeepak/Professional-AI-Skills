---
name: security-architecture-review
description: Review a system or proposed architecture for trust boundaries, identity, data flows, attack paths, control placement, resilience, and operational evidence. Use when assessing a solution design, preparing a security design review, evaluating cloud or SaaS integrations, approving an exception, or converting architecture risks into prioritized engineering actions.
---

# Security Architecture Review

## Operating standard

Review the architecture that exists or is proposed, not an imagined reference architecture. Separate confirmed facts, design assumptions, missing evidence, threats, and recommendations. Do not label a product or protocol secure without examining its configuration and operating context.

## Inputs

Obtain the business purpose, users and actors, system context, data classification, components, trust boundaries, identities, interfaces, network paths, deployment model, secrets, logging, dependencies, recovery requirements, and known constraints.

## Workflow

1. Define the protected outcomes and unacceptable failure modes.
2. Draw or restate components, actors, data flows, and trust boundaries.
3. Identify entry points, privileges, sensitive transitions, and external dependencies.
4. Trace misuse and attack paths across identity, application, data, infrastructure, and operations.
5. Evaluate preventive, detective, responsive, and recovery controls at each material path.
6. Test least privilege, segmentation, secure defaults, failure isolation, and evidence quality.
7. Rank findings by exploit preconditions, exposure, blast radius, detectability, and business consequence.
8. Recommend design changes, compensating controls, verification steps, and accountable owners.

## Decision rules

- A control claim requires configuration or operational evidence, not a product feature list.
- Treat identity and authorization paths as first-class architecture.
- Elevate risks that cross tenant, administrative, production, or sensitive-data boundaries.
- Distinguish must-fix approval blockers from hardening improvements.
- Accept a compensating control only when it addresses the same failure path and can be monitored.

## Output

Provide:

1. Architecture and trust-boundary summary
2. Assumptions and evidence gaps
3. Material attack paths
4. Findings ranked by consequence and feasibility
5. Required changes and compensating controls
6. Verification plan and approval conditions
7. Residual risk and named risk owner when known

## Quality check

- Findings reference a component, flow, boundary, or operating process.
- Recommendations are testable and proportionate.
- Severity is not based on generic threat labels alone.
- Logging, key management, administrative access, and recovery are covered.
- The result clearly states approve, approve with conditions, or redesign.

## Failure recovery

If diagrams or configurations are missing, produce a bounded review of known elements plus a targeted evidence request. Do not fill gaps with a generic checklist and call it an assessment.

## Example

**Request:** “Review this AI service that sends customer documents to a third-party model API.”

Trace data, identity, retention, tenant isolation, failure, and monitoring paths; identify approval blockers and verification evidence.

## Evaluation

A strong result is architecture-specific, threat-informed, testable, and clear about approval conditions.

## Related skills

Use `threat-modeling` for abuse cases, `architecture-review` for broader system quality, and `third-party-risk` for supplier controls.
