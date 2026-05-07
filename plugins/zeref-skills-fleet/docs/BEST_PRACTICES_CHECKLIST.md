# Zeref Skills Fleet Best Practices Checklist

## Claude/Agent Skill Compliance

- [x] Each skill lives in its own folder.
- [x] Each folder contains a `SKILL.md`.
- [x] YAML frontmatter includes `name` and `description`.
- [x] Folder names match skill names.
- [x] Names are lowercase kebab-case.
- [x] Descriptions are written to trigger only when relevant.
- [x] Skill bodies load only when needed, keeping global context light.

## Plugin Packaging

- [x] Root marketplace manifest exists.
- [x] Plugin manifest exists.
- [x] Marketplace source points to the plugin directory.
- [x] Version alignment prevents update detection problems.
- [x] Scripts validate metadata, counts, folders, and JSON.

## Output Optimization

- [x] Smallest useful skill stack: one lead, one to three support skills, one QA/final gate.
- [x] Caveman compression only for long/messy contexts.
- [x] Token budget rules embedded in every skill.
- [x] Handoff summaries reduce re-reading cost.
- [x] No duplicate deliverables unless explicitly requested.

## Trust and Evidence

- [x] Facts, assumptions, unknowns, and risks are separated.
- [x] Unsupported claims cannot be presented as facts.
- [x] Source validation and citation QA are assigned to final/hq research skills.
- [x] Synthetic research must be labeled.

## Execution Governance

- [x] No publishing, sending, deletion, movement, scheduling, or irreversible changes without explicit approval.
- [x] Notion and Linear update blocks are generated when direct connector access is unavailable.
- [x] QA and final compiler layers exist for end-to-end project closure.
