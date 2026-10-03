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


## Run in VS Code
1. Open this repository folder in VS Code.
2. Install the recommended Python extension.
3. Install the project with python -m pip install -e .
4. Press F5 and choose Run Universal Language Compiler.
5. Chrome opens automatically.
6. Type what you want to build.
7. Pick the programming language from the dropdown.
8. Press GENERATE CODE and copy the result.

You do not need to use the terminal for normal use anymore. The browser is the main interface.
