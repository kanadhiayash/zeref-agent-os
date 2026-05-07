# Caveman Compression Protocol

Use Caveman compression only when context is long, duplicated, messy, or token-heavy.

Preserve exactly:

- Names
- URLs
- File paths
- Commands
- Version numbers
- Error messages
- User constraints
- Decisions
- Safety warnings

Compress:

- Repeated explanation
- Motivational language
- Framework fluff
- Already-resolved debate
- Low-signal context

Output format:

```markdown
# Compressed Context Brief

## Objective
## Hard Constraints
## Verified Facts
## Decisions Already Made
## Open Questions
## Required Next Action
```
