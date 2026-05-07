# Release Checklist v1.1.2

1. Run validation:

```bash
python plugins/zeref-skills-fleet/scripts/validate_zeref_package.py .
```

2. Commit all changes:

```bash
git add .
git commit -m "Release Zeref Skills Fleet v1.1.2"
git push origin main
```

3. Tag release:

```bash
git tag v1.1.2
git push origin v1.1.2
```

4. In Claude Code:

```bash
/plugin marketplace update
/plugin update zeref-skills-fleet
/reload-plugins
```

5. Confirm `/plugin` shows version `1.1.2`.
