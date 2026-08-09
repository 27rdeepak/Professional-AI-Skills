# Changelog

Notable changes follow Keep a Changelog and Semantic Versioning.

## [Unreleased]

### Added

- 12 production-ready skills for security strategy and architecture, compliance readiness, disaster recovery, SaaS governance, Microsoft 365 governance, leadership, and human oversight of AI.
- Regression cases for recovery evidence, meaningful AI oversight, compliance readiness, and delegation quality.
- Non-breaking quality-lint in the repository validator that flags generic boilerplate descriptions, placeholder examples, and self-referential cross-links (surfaced as warnings; does not fail the build).
- Executable forward-test runner (`scripts/run_checks.py`) that enforces the per-skill contract — concrete triggers, a real multi-step workflow, a bounded output, a worked example, named failure modes, resolving cross-links, and agent metadata — plus a global check that every skill named in the regression suite exists. Wired into the Validate CI workflow; 112/112 skills pass.

### Changed

- Rewrote 44 shallow-legacy skills across core reasoning, cybersecurity, business, enterprise IT, Microsoft 365, communication, leadership, and research with concrete trigger language, domain-specific workflows, tailored failure modes, worked examples, corrected cross-links, and specific agent prompts.
- Replaced generic descriptions with concrete triggers on 56 additional skills that already had domain-specific workflows and examples.
- Removed all placeholder examples ("analyze this material"), empty one-line workflow stubs, and self-referential related-skills links repository-wide; every skill now states concrete triggers and carries a real procedure and example. Closes the 1.1 roadmap item on replacing shallow legacy workflows.
- Rebuilt the bodies of 56 middle-tier skills (ai-product, business, communication, productivity, research, software-engineering) that had a real description but a stub `Combine with ...` workflow and no example or failure-modes section: each now has a domain-specific 6-step workflow, a named output artifact, tailored failure modes, and a worked example.

## [0.1.0] - 2026-07-26

### Added in 0.1.0

- Repository governance, validation, platform guidance, and 20 initial skills.

## [0.2.0] - 2026-07-26

### Added in 0.2.0

- Enterprise IT, Microsoft 365, cybersecurity, business, and leadership skills.
- Frameworks, templates, personas, playbooks, evaluation files, and platform guidance.

## [0.3.0] - 2026-07-26

### Added in 0.3.0

- Remaining core skills to reach 100 production-ready skills.
- Phase 5 examples and regression suite.

## [1.0.0] - 2026-07-26

### Added in 1.0.0

- Release notes and packaging for the 100-skill AIOS library.
- Stable repository structure with examples, regressions, and platform guidance.
