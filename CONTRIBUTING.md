# Contributing

1. Keep the IR language-neutral.
2. Add tests for parser and backend changes.
3. Never add hard-coded credentials.
4. Document new language features.
5. Reject ambiguous input rather than inventing behavior.
6. Keep target generators small and readable.

To add a target, create a backend in `targets/`, register it in `targets/__init__.py`, add tests, and update `docs/LANGUAGES.md`.
