# Coding Standards

Enforced by Daniel during code review and development. Not suggestions — rules.
If a language isn't listed here, Daniel auto-detects conventions from the project and follows them.

## Universal Rules (Every Language)

### Security
- Never hardcode secrets, API keys, or passwords. Use environment variables.
- Validate user input at system boundaries. Trust nothing from outside.
- Sanitize data before rendering (prevent XSS).
- Use parameterized queries (prevent SQL injection).
- Never commit `.env` files. `.gitignore` must cover them.
- Pin dependency versions. Review new dependencies before adding.

### Functions
- One function, one job. If you need "and" to describe it, split it.
- Max 40 lines per function. Extract if longer.
- Max 3 parameters. Use an options/config object if more.
- Pure functions where possible — same input, same output, no side effects.
- Early returns over deep nesting.

### Files
- Max 300 lines per file. Split if larger.
- One component/class/module per file.
- Group by feature, not by type.
- Index/barrel files only for re-exports, no logic.

### Naming
- Names should describe WHAT, not HOW.
- Functions: verb-first (`getUser`, `validateInput`, `handleSubmit`).
- Booleans: prefix with `is`, `has`, `should`, `can`.
- Constants: `UPPER_SNAKE_CASE` for true constants.
- Be consistent within the project. Match existing patterns.

### Error Handling
- Never swallow errors silently. Log or re-throw.
- Specific error messages, not generic "Something went wrong."
- Handle errors at the right level — don't catch too early.
- Always handle async errors and promise rejections.

### Git
- Commit messages: imperative mood, under 72 chars, explain WHY.
- One logical change per commit.
- Never commit generated files, node_modules, build artifacts, or secrets.
- Branch names: `feature/short-description`, `fix/short-description`.

### Testing
- Test behavior, not implementation.
- Name tests: `should [behavior] when [condition]`.
- Cover: happy path, edge cases, error cases.
- Tests must be deterministic — no flaky tests.

---

## Language-Specific Rules

### TypeScript / JavaScript
- `const` over `let`. Never `var`.
- Strict equality (`===`), never loose (`==`).
- Optional chaining (`?.`) and nullish coalescing (`??`).
- Files: `kebab-case`. Components: `PascalCase`. Variables: `camelCase`.
- Prefer `async/await` over `.then()` chains.

### React
- Functional components only.
- Custom hooks for shared logic (`useX` naming).
- Components under 150 lines.
- Avoid prop drilling — use context or composition.
- Memoize expensive computations, not everything.
- Colocate styles, tests, and types with components.

### Python
- Type hints on function signatures.
- Dataclasses or Pydantic for structured data.
- List comprehensions over `map`/`filter` for readability.
- `pathlib` over `os.path`.
- Files: `snake_case`. Classes: `PascalCase`. Variables: `snake_case`.

### Go
- Accept interfaces, return structs.
- Handle errors explicitly — no naked returns after `if err != nil`.
- Use `context.Context` for cancellation and timeouts.
- Table-driven tests.
- Files: `snake_case`. Exported: `PascalCase`. Unexported: `camelCase`.

### Rust
- Prefer `Result` and `Option` over panics.
- Use `clippy` warnings as errors.
- Implement `Display` for custom error types.
- Prefer iterators over manual loops.
- Follow the Rust API Guidelines.

### SQL
- Uppercase keywords (`SELECT`, `FROM`, `WHERE`).
- Parameterized queries always — never string concatenation.
- Name constraints and indexes explicitly.
- Use migrations, not manual DDL.

---

## When In Doubt

If a rule isn't listed for a language:
1. Check the project's existing conventions first
2. Check the language's official style guide
3. Pick the simplest, most readable option
4. Document the choice in `memory/decisions.md`
