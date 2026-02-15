# Coding Standards (Condensed)

Universal rules enforced by Daniel. For full language-specific rules, see the attached standards document.

## Security
- Never hardcode secrets/API keys. Use environment variables.
- Validate user input at system boundaries. Trust nothing from outside.
- Sanitize data before rendering (prevent XSS). Use parameterized queries (prevent SQL injection).
- Never commit `.env` files. Pin dependency versions.

## Functions
- One function, one job. If you need "and" to describe it, split it.
- Max 40 lines per function. Max 3 parameters (use config object if more).
- Pure functions where possible. Early returns over deep nesting.

## Files
- Max 300 lines per file. One component/class/module per file.
- Group by feature, not by type. Index files only for re-exports.

## Naming
- Names describe WHAT, not HOW. Functions: verb-first (getUser, validateInput).
- Booleans: prefix with is/has/should/can. Constants: UPPER_SNAKE_CASE.

## Error Handling
- Never swallow errors silently. Specific error messages, not generic ones.
- Handle errors at the right level. Always handle async errors and promise rejections.

## Git
- Commit messages: imperative mood, under 72 chars, explain WHY.
- One logical change per commit. Never commit generated files, node_modules, or secrets.

## Testing
- Test behavior, not implementation. Name: "should [behavior] when [condition]".
- Cover: happy path, edge cases, error cases. Tests must be deterministic.
