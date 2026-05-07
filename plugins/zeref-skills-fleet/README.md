# Zeref Skills Fleet Plugin

Version: `1.1.2`

This plugin contains the installable Zeref Skills Fleet for Claude Code.

## Use

After installation, skills are namespaced under the plugin name. Example:

```text
/zeref-skills-fleet:zeref-hq-fleet-activator
/zeref-skills-fleet:zeref-system-marketplace-packager
```

Claude may also invoke skills automatically when their descriptions match the task context.

## Best Routing Rule

Use the smallest useful stack:

- 1 lead skill
- 1-3 support skills
- 1 QA/final gate

Use Caveman compression only when context is long, messy, duplicated, or token-heavy.
