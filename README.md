# Universal Language Compiler

Translate controlled human-language programming instructions into 10 programming languages.

## Targets

Python, C, C++, Java, C#, JavaScript, Visual Basic, SQL, R, Rust.

## Pipeline

Human language -> parser -> Universal Intermediate Representation (IR) -> target backend -> generated source.

The first release is deterministic and intentionally rejects ambiguous instructions. Future versions can add local NLP models, Tree-sitter parsing, LLVM/WebAssembly backends, and CPU-specific machine-code toolchains.

## Quick start

Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m cli.main translate "print hello world" --target python
python -m cli.main translate "create a variable called speed equal to 100" --target cpp
```

On Windows use `.venv\\Scripts\\activate`.

## Supported instructions

- print/display/say text
- create or assign variables
- simple if comparisons with print
- simple repeat loops
- SQL table creation

Generated code is never executed automatically. Review and test it before compiling or running it.

## License

MIT.
