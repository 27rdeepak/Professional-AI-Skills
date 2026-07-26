# Contributing

1. Search existing skills and issues for overlap.
2. Open a “New skill” issue for a new capability.
3. Use a lowercase hyphenated folder under the best category.
4. Keep only `name` and `description` in `SKILL.md` frontmatter; put all triggers in the description.
5. Write concise imperative instructions and add resources only for repeated work.
6. Add matching `agents/openai.yaml`.
7. Run `python3 scripts/validate_repository.py`.

Follow the [specification](docs/skill-specification.md), [style guide](docs/style-guide.md), and [Code of Conduct](CODE_OF_CONDUCT.md). Reviewers assess distinctness, decision utility, safety, context cost, neutrality, and testability—not file count.
