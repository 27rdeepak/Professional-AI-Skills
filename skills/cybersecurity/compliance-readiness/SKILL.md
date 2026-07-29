---
name: compliance-readiness
description: Assess readiness for a security, privacy, or technology audit by mapping obligations to scoped systems, control ownership, implementation evidence, testing, and remediation. Use when preparing for SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR-related assurance, customer audits, internal audits, or deciding whether an organization is ready to enter formal assessment.
---

# Compliance Readiness

## Operating standard

Treat compliance as evidence-backed operating behavior, not document completion. Do not provide legal conclusions. Distinguish applicability, control design, implementation, operating effectiveness, and evidence sufficiency.

## Inputs

Obtain the target framework and version, audit type and period, scope, legal or contractual drivers, systems and locations, control owners, prior findings, policies, technical evidence, sampling requirements, auditor expectations, and deadline.

## Workflow

1. Confirm framework applicability, assessment boundary, period, and exclusions.
2. Build a traceable requirement-to-control map without inventing equivalence.
3. Identify control owners, systems, frequency, populations, and evidence sources.
4. Test whether each control is designed, implemented, consistently operated, and evidenced.
5. Evaluate evidence for authenticity, period coverage, completeness, and reproducibility.
6. Classify gaps as scope, design, implementation, operation, evidence, or governance failures.
7. Prioritize remediation by audit impact, security consequence, dependency, and lead time.
8. Define retesting, sampling, exception handling, and executive acceptance.

## Decision rules

- Mark a requirement not applicable only with a documented scope or legal basis.
- Do not mark a control effective because a policy exists.
- Evidence outside the audit period cannot prove in-period operation.
- Automated evidence still requires source integrity and understandable ownership.
- Escalate repeated exceptions and unsupported management assertions.

## Output

Provide:

1. Readiness verdict and confidence
2. Scope and applicability assumptions
3. Control status matrix
4. Evidence quality and coverage gaps
5. Prioritized remediation plan with owners and dates
6. Retest and audit-entry criteria
7. Executive risks and decisions

## Quality check

- Framework version, scope, period, and evidence dates are explicit.
- Status labels have observable definitions.
- Gaps are not hidden inside an aggregate percentage.
- Remediation addresses the cause, not only the missing artifact.
- The readiness verdict states what could materially change it.

## Failure recovery

If control evidence is incomplete, issue a provisional readiness view with a precise evidence request. If applicability is legally uncertain, identify the decision point and route it to qualified counsel.

## Example

**Request:** “Are we ready for a SOC 2 Type II audit starting next quarter?”

Assess operating history, evidence coverage, control exceptions, and remediation lead time; do not answer with a policy checklist alone.

## Evaluation

A strong result is scoped, traceable, evidence-tested, and clear about audit-entry conditions.

## Related skills

Use `evidence-validation` for contested artifacts, `security-program-strategy` for systemic gaps, and `risk-communication` for executives.
