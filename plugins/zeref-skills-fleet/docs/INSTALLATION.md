# Installation Guide — Zeref Skills Fleet v1.1.2

## Local test

```bash
python plugins/zeref-skills-fleet/scripts/validate_zeref_package.py .
claude --plugin-dir ./plugins/zeref-skills-fleet
/reload-plugins
```

## Marketplace install after pushing repo

```bash
/plugin marketplace add https://github.com/kanadhiayash/zeref-skills-fleet
/plugin marketplace update
/plugin install zeref-skills-fleet@zeref-skills
/reload-plugins
```

## Update path

```bash
/plugin marketplace update
/plugin update zeref-skills-fleet
/reload-plugins
```

If update does not show, confirm that `plugins/zeref-skills-fleet/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` both show `1.1.2` and that the repo branch/tag being used contains the new commit.
