# Architecture

1. Input parser converts a controlled natural-language instruction into IR.
2. Universal IR stores language-neutral operations.
3. Target backends convert IR to source code.
4. Validation catches unsupported operations before generation.

Backends stay independent from the natural-language parser. Future versions can add Tree-sitter parsing, local NLP models, LLVM IR, WebAssembly, and CPU-specific code generation.
