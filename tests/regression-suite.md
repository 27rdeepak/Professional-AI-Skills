# Regression Suite

## Must-hold behaviors

1. Skills must keep `SKILL.md` frontmatter to `name` and `description` only.
2. Skill descriptions must include concrete trigger language.
3. Outputs must preserve dates, units, and source context when supplied.
4. Decision skills must distinguish facts, inference, and recommendation.
5. High-stakes skills must include risks and a next test when evidence is incomplete.

## Representative checks

### Evidence handling

Prompt:
`Use $research-synthesizer to combine these conflicting sources.`

Expected:
- Mentions disagreement explicitly
- Shows uncertainty instead of over-claiming
- Cites which source types matter most

### Operational decision

Prompt:
`Use $it-service-management to review our incident queue.`

Expected:
- Identifies bottlenecks, ownership, and service impact
- Avoids generic process advice
- Recommends a concrete operating change

### Security prioritization

Prompt:
`Use $vulnerability-management to prioritize 200 findings.`

Expected:
- Uses exposure and business context
- Separates severity from risk
- Produces an actionable ordering

### Executive communication

Prompt:
`Use $executive-writer to brief the CIO on a release delay.`

Expected:
- Bottom line first
- Risks and options clearly separated
- Direct and concise language

### Recovery evidence

Prompt:
`Use $disaster-recovery-planning to assess whether successful backup jobs prove we can recover a critical service.`

Expected:
- Separates backup success from service recoverability
- Maps identity, network, data, supplier, and operational dependencies
- Requires restore or recovery test evidence
- States unverified residual risk

### Human oversight

Prompt:
`Use $human-in-the-loop-design to add human approval to a high-volume AI decision process.`

Expected:
- Defines what the human intervention is intended to prevent or correct
- Tests reviewer capacity, authority, automation bias, and fallback
- Avoids treating a human click as sufficient oversight
- Measures both model and reviewer performance

### Compliance readiness

Prompt:
`Use $compliance-readiness to decide whether policies alone make us ready for a SOC 2 Type II audit.`

Expected:
- Separates design, implementation, operation, and evidence
- Checks audit period and scope
- Identifies remediation and retest criteria
- Avoids legal conclusions

### Delegation quality

Prompt:
`Use $delegation-design to delegate a high-visibility renewal without micromanaging it.`

Expected:
- Defines outcome and non-negotiable constraints
- Aligns authority, accountability, resources, and checkpoints
- Preserves room for a different valid method
- Makes escalation triggers explicit
