# Changelog

## [1.1.2] - 2026-05-07

### Added
- Added 6 system governance skills for routing, compression, token budgeting, evidence memory, marketplace packaging, and update diagnosis.
- Added root marketplace manifest at `.claude-plugin/marketplace.json`.
- Added plugin manifest at `plugins/zeref-skills-fleet/.claude-plugin/plugin.json`.
- Added validation script and GitHub Actions workflow.
- Added release, marketplace, best-practices, security, Notion/Linear, and Caveman protocol docs.

### Changed
- Synchronized version to `1.1.2` across marketplace, plugin manifest, changelog, and package docs.
- Standardized all skill folders as lowercase kebab-case with `SKILL.md`.
- Embedded token discipline, anti-hallucination, Notion update, Linear ticket, and handoff behavior across all skills.

### Fixed
- Fixed update-detection risk by ensuring `plugin.json` has a bumped semantic version. Claude Code only surfaces updates when the plugin version changes when explicit versioning is used.
