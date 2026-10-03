# Universal Language Compiler

A deterministic human-language programming translator. You write supported instructions in normal English and choose one of 10 target languages.

## Targets

Python, C, C++, Java, C#, JavaScript, Visual Basic, SQL, R, Rust.

## Important: no AI is required

ULC is intentionally back to the original deterministic design. It does **not** require Ollama, a local AI model, a cloud API, or an internet connection for translation.

That makes the translator predictable and lightweight. The tradeoff is simple: it can understand the English command patterns documented here, but it cannot magically understand an unlimited arbitrary software specification. Add a new parser rule when you want a new deterministic command.

## Quick start

Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m cli.main translate "print hello world" --target python
python -m cli.main translate "set speed equal to 100; increase speed by 10; print done" --target cpp
```

On Windows use `.venv\\Scripts\\activate`.

## Browser mode

Double-click `START.bat`. It checks for Python, installs the project, starts the local web interface, and opens Chrome.

No Ollama setup is needed.

## Supported English commands

### Output

- `print hello world`
- `display hello world`
- `say hello world`
- `show hello world`
- `output hello world`
- `echo hello world`
- `write hello world`

### Variables

- `create a variable called score equal to 10`
- `make variable score equals 10`
- `set score = 10`
- `define score equal to 10`
- `declare variable score equal 10`

### Input

- `ask for name`
- `input name`
- `get name with prompt Enter your name`

### Math

- `add 5 to score`
- `subtract 2 from score`
- `multiply 3 by score`
- `divide 2 by score`
- `increase score by 1`
- `decrease score by 1`

### Conditions

- `if age is greater than 18 then print adult`
- `if age is less than 18 then print minor`
- `if age is equal to 18 then print adult`
- `if age is not equal to 18 then print different`
- `if age is at least 18 then print adult`
- `if age is at most 18 then print adult`

### Loops

- `repeat 5 times print hello`
- `loop 5 times print hello`
- `run 5 x print hello`
- `while score is less than 10 then print waiting`

### Utilities

- `wait 2 seconds`
- `sleep 1 second`
- `pause 3 seconds`
- `generate random number from 1 to 100`
- `generate random number from 1 to 100 and store it in number`
- `clear`
- `comment: this is my program`

### SQL

- `create table users with id integer, name varchar(100)`
- `make a table products having id integer, price decimal(10,2)`

## Multiple commands

Put commands on separate lines or separate them with semicolons:

```
set score equal to 10
increase score by 5
if score is at least 15 then print high score
```

or:

```
set score equal to 10; increase score by 5; print done
```

## What this project is and is not

ULC is a command-based deterministic translator, not a general-purpose AI coding assistant. This is intentional. It means the same input follows the same parser rules every time and there is no local model to install.

The parser and target backends are separate, so adding a new English command means adding an intermediate operation and its translations rather than adding an AI dependency.

Generated code is never executed automatically. Review and test it before compiling or running it.

## Project structure

- `core/parser.py` — understands English command patterns.
- `core/ir.py` — stores the common intermediate representation.
- `core/translator.py` — runs parsing, validation, and target generation.
- `targets/` — the 10 language backends.
- `web.py` — Chrome/browser interface.
- `cli/` — command-line interface.
- `tests/` — automated tests.
- `START.bat` — simple Windows launcher.

## Troubleshooting

### Chrome does not open

Open the printed local address manually. The server only listens on your own computer.

### A command is not recognized

Check the supported command list above. ULC does not use AI fallback. If you want a new phrase supported, add a deterministic parser rule and a test.

### Generated code is not what you expected

Check the exact English wording and target language. ULC translates the supported operation into a target-language template; it does not infer an unlimited software design.

## License

MIT.
