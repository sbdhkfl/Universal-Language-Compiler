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


## Broad English mode

The original deterministic parser is still included for fast, predictable simple commands. For normal English requests such as "build a calculator", "make a to-do app", "create a game", or other larger descriptions, the browser can use a local coding AI through Ollama.

On Windows, run setup_ai.bat once. It installs Ollama when possible and downloads the local coding model. Then run the project normally.

The local AI runs on your computer instead of sending your code request to a paid cloud API. Because AI-generated code can contain mistakes, review and test generated code before running it.

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


## Browser mode (the normal way to use ULC)

The Universal Language Compiler now has a browser interface. You can use normal English instead of memorizing special commands.

### Start it

1. Open the repository in VS Code.
2. Install the project:
   `python -m pip install -e .`
3. Press **F5** and choose **Run Universal Language Compiler**.
4. Chrome opens automatically.
5. Type what you want to build.
6. Select the programming language.
7. Press **GENERATE CODE**.

The terminal is still available for developers, but you do not need it for normal use.

## Broad English mode

The original deterministic compiler handles simple instructions quickly and predictably. When an instruction is more complex or does not match those rules, ULC can use an optional **local coding AI through Ollama**.

This means requests can be written as normal English, for example:

- "Build a calculator with add, subtract, multiply, and divide."
- "Create a to-do app with tasks I can add, edit, and delete."
- "Make a Python game where the player collects coins."
- "Create a website with a home page, login page, and dashboard."
- "Write a program that reads a CSV file and calculates statistics."

### Set up the local AI on Windows

Run:

`setup_ai.bat`

once from the repository folder. It installs Ollama when possible and downloads the configured local coding model.

The default model is `qwen2.5-coder:3b`. You can change it with the `ULC_OLLAMA_MODEL` environment variable.

The local AI runs on your own computer rather than sending the programming request to a paid cloud API.

### Important

AI-generated code can contain mistakes. **Always review and test generated code before running it.** ULC does not automatically execute generated programs.

Never put passwords, API keys, access tokens, or private tokens into prompts or generated source code.
