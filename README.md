# Zeref Skills Fleet v1.1.2

AI Product, Design, Development, Marketing & Operations Skills for Claude.

This repository is packaged as a Claude Code plugin marketplace plus a plugin bundle. It includes **112 installable skills**: the original 106 Zeref employee skills plus 6 v1.1.2 system governance skills for routing, Caveman compression, token budgeting, evidence memory, marketplace packaging, and update diagnosis.

## Repository Layout

```text
.claude-plugin/marketplace.json
plugins/zeref-skills-fleet/.claude-plugin/plugin.json
plugins/zeref-skills-fleet/skills/<skill-name>/SKILL.md
plugins/zeref-skills-fleet/agents/*.md
plugins/zeref-skills-fleet/commands/*.md
plugins/zeref-skills-fleet/docs/*.md
plugins/zeref-skills-fleet/manifests/*
plugins/zeref-skills-fleet/scripts/validate_zeref_package.py
```

## Install in Claude Code

```bash
/plugin marketplace add https://github.com/kanadhiayash/zeref-skills-fleet
/plugin marketplace update
/plugin install zeref-skills-fleet@zeref-skills
/reload-plugins
```

For local testing before publishing:

```bash
claude --plugin-dir ./plugins/zeref-skills-fleet
/reload-plugins
```

## Command Center

Notion Board: https://copper-tv-288.notion.site/Zeref-Skills-Fleet-Command-Center-358d695d836a81af9f6adf30770217c3

## Release

Current version: `1.1.2`

The version is intentionally synchronized across:

- root `VERSION`
- root `.claude-plugin/marketplace.json`
- plugin `.claude-plugin/plugin.json`
- `CHANGELOG.md`
- release checklist docs
