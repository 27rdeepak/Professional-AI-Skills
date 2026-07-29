---
name: exchange-online-governance
description: Assess and govern Exchange Online across mail flow, authentication, delegated access, transport rules, external forwarding, retention, shared mailboxes, protection, resilience, and support operations. Use when reviewing Microsoft 365 email security, troubleshooting governance gaps, preparing an audit, designing administrative controls, or planning Exchange Online policy and lifecycle improvements.
---

# Exchange Online Governance

## Operating standard

Distinguish configured policy from effective coverage and observed mail flow. Do not recommend changes without considering licensing, hybrid dependencies, business processes, incident response, and user impact.

## Inputs

Obtain tenant topology, licensing, domains, hybrid or relay dependencies, mailbox types, privileged roles, authentication settings, transport and inbox rules, connectors, forwarding, protection policies, retention, audit settings, incidents, and support ownership.

## Workflow

1. Define business mail flows, critical mailboxes, external dependencies, and failure impact.
2. Review administrative roles, delegated access, shared mailbox ownership, and lifecycle controls.
3. Trace inbound, outbound, application, relay, and partner mail paths.
4. Assess domain authentication, spoof protection, malware and phishing controls, and exception scope.
5. Review external forwarding, transport rules, connectors, allow lists, and auto-forwarding abuse paths.
6. Assess retention, holds, auditing, message trace access, and investigation readiness.
7. Evaluate service continuity, communications, support escalation, and change control.
8. Prioritize configuration, monitoring, ownership, and user-impact actions.

## Decision rules

- Treat broad allow rules and unauthenticated relay paths as high scrutiny items.
- Confirm SPF, DKIM, and DMARC alignment by domain and sending service before declaring coverage.
- Do not remove legacy or application mail paths without an owner and tested replacement.
- Separate mailbox delegation required for operations from convenience access.
- Verify that audit and retention recommendations match licensing and legal requirements.

## Output

Provide:

1. Mail-flow and dependency summary
2. Identity and administrative control findings
3. Protection and authentication coverage
4. Delegation, forwarding, rule, and connector risks
5. Retention, audit, and investigation readiness
6. Prioritized changes with testing and rollback
7. Owners, metrics, and review cadence

## Quality check

- Findings name affected domains, flows, policies, or mailbox populations.
- Recommendations include user and application impact.
- Exceptions, overrides, and monitoring gaps are visible.
- Licensing and hybrid assumptions are stated.
- Changes include validation and rollback steps.

## Failure recovery

If tenant exports are unavailable, produce a targeted evidence collection plan and a provisional review based only on supplied facts.

## Example

**Request:** “Review Exchange Online after several spoofing incidents and uncontrolled shared mailbox access.”

Assess domain authentication, policy coverage, exceptions, delegation, evidence, and operating ownership.

## Evaluation

A strong result is tenant-specific, mail-flow aware, safe to implement, and operationally measurable.

## Related skills

Use `entra-id-governance` for identity controls, `defender-operations` for detection, and `compliance-readiness` for evidence.
