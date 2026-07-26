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
