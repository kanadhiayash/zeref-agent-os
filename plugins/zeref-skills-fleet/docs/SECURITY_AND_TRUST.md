# Security and Trust Notes

- Do not commit secrets, API keys, `.env` files, private tokens, personal documents, or private workspace exports.
- Treat plugin installation as trusted-code installation.
- Keep hooks, MCP servers, and monitors conservative unless the user explicitly enables them.
- This package includes no executable hook, MCP, or monitor by default.
- The validation script reads local files only.
