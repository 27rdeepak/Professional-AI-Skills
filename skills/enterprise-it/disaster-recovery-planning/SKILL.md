---
name: disaster-recovery-planning
description: Design and assess technology recovery capabilities by mapping critical services, dependencies, recovery objectives, backup integrity, failover procedures, roles, communications, and test evidence. Use when creating a disaster recovery plan, reviewing RTO and RPO commitments, preparing resilience exercises, assessing backup or failover readiness, or prioritizing recovery investments.
---

# Disaster Recovery Planning

## Operating standard

Base recovery claims on dependency mapping and demonstrated tests. Distinguish business continuity, disaster recovery, high availability, backup, cyber recovery, and incident response. Never treat a successful backup job as proof of recoverability.

## Inputs

Obtain critical business services, impact tolerances, RTO and RPO targets, applications and infrastructure, data flows, identity and network dependencies, suppliers, backup architecture, recovery procedures, staffing, communication paths, prior test results, and regulatory commitments.

## Workflow

1. Rank business services by impact over time and define minimum viable service.
2. Validate RTO, RPO, and maximum tolerable outage with business owners.
3. Map applications, data, identity, network, facilities, people, and supplier dependencies.
4. Identify recovery strategies, failure domains, capacity assumptions, and control-plane dependencies.
5. Review backup immutability, isolation, credentials, retention, restoration sequence, and integrity verification.
6. Define invocation criteria, command roles, technical runbooks, communications, and escalation.
7. Design tests from component restoration through service-level and crisis exercises.
8. Record gaps, investment choices, residual risk, and retest dates.

## Decision rules

- Reject RTO or RPO targets that lack business ownership or technical feasibility.
- Prioritize shared dependencies that can block multiple service recoveries.
- Require restore evidence for critical data and rebuild evidence for critical infrastructure.
- Test degraded operating modes and upstream or downstream supplier failure.
- Separate planned failover success from recovery under destructive or credential-compromise scenarios.

## Output

Provide:

1. Recovery scope and business impact summary
2. Service tiers with validated RTO/RPO
3. Dependency and single-point-of-failure map
4. Recovery strategies and runbook gaps
5. Test program and acceptance criteria
6. Investment priorities and residual risk
7. Action register with owners and dates

## Quality check

- Recovery objectives link to business impact.
- Critical identity, DNS, network, key, and administrative dependencies are included.
- The plan states who can declare a disaster and how authority transfers.
- Test evidence includes duration, data loss, defects, and remediation.
- Manual steps, specialist dependencies, and unavailable assumptions are visible.

## Failure recovery

If business impact data is absent, propose provisional tiers and schedule validation before promising recovery targets. If testing is impossible, state the unverified risk and design the smallest safe proof.

## Example

**Request:** “Assess whether our SaaS-heavy environment can recover from a tenant-wide identity compromise.”

Trace control-plane, identity, backup, communication, supplier, and administrative recovery dependencies and define a scenario test.

## Evaluation

A strong result is service-led, dependency-aware, testable, and explicit about unproven recovery claims.

## Related skills

Use `incident-response` for crisis actions, `enterprise-asset-inventory` for dependencies, and `risk-analysis` for residual risk.
