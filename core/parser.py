import re
from .errors import TranslationError
from .ir import Program

NUMBER = r"-?\d+(?:\.\d+)?"
NAME = r"[A-Za-z_]\w*"

def _literal(value):
    value = value.strip().rstrip(".")
    if re.fullmatch(NUMBER, value):
        return float(value) if "." in value else int(value)
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value

def _split_commands(text):
    # New lines and semicolons let one request contain several deterministic commands.
    return [part.strip() for part in re.split(r"[;\n]+", text) if part.strip()]

def _parse_one(text, program):
    # Comments
    m = re.fullmatch(r"(?:comment|note|remark)\s*:?\s*(.+)", text, re.I)
    if m:
        program.add("comment", value=m.group(1)); return

    # Output
    m = re.fullmatch(r"(?:print|display|say|show|output|echo|write)\s+(.+)", text, re.I)
    if m:
        program.add("print", value=_literal(m.group(1))); return

    # Input
    m = re.fullmatch(r"(?:ask|input|get)\s+(?:for\s+)?(?:a\s+)?(?:value\s+)?(?:into\s+|called\s+)?("+NAME+r")(?:\s+with\s+(?:prompt\s+)?(.+))?", text, re.I)
    if m:
        program.add("input", name=m.group(1), prompt=_literal(m.group(2) or "Enter a value:")); return

    # Variable assignment
    m = re.fullmatch(r"(?:create|make|set|define|declare)\s+(?:a\s+)?(?:variable|var)\s+(?:called\s+|named\s+)?("+NAME+r")\s+(?:equal\s+to|equals|=|equal\s+)(.+)", text, re.I)
    if m:
        program.add("assign", name=m.group(1), value=_literal(m.group(2))); return

    # Arithmetic assignment: add/subtract/multiply/divide a number from a variable
    m = re.fullmatch(r"(add|subtract|multiply|divide)\s+(.+?)\s+(?:to|from|by)\s+("+NAME+r")", text, re.I)
    if m:
        action, amount, name = m.group(1).lower(), _literal(m.group(2)), m.group(3)
        if action == "add": op = "+"
        elif action == "subtract": op = "-"
        elif action == "multiply": op = "*"
        else: op = "/"
        program.add("math", name=name, op=op, value=amount); return

    m = re.fullmatch(r"(?:increase|increment)\s+("+NAME+r")(?:\s+by\s+(.+))?", text, re.I)
    if m:
        program.add("math", name=m.group(1), op="+", value=_literal(m.group(2) or "1")); return
    m = re.fullmatch(r"(?:decrease|decrement)\s+("+NAME+r")(?:\s+by\s+(.+))?", text, re.I)
    if m:
        program.add("math", name=m.group(1), op="-", value=_literal(m.group(2) or "1")); return

    # If condition -> output
    m = re.fullmatch(
        r"if\s+("+NAME+r")\s+(?:is\s+)?(greater than|less than|equal to|equals|not equal to|at least|at most)\s+(.+?)\s+(?:then\s+)?(?:print|display|say|show|output|echo)\s+(.+)",
        text, re.I)
    if m:
        ops={"greater than":">","less than":"<","equal to":"==","equals":"==","not equal to":"!=","at least":">=","at most":"<="}
        program.add("if_print", name=m.group(1), op=ops[m.group(2).lower()], compare=_literal(m.group(3)), value=_literal(m.group(4))); return

    # Repeat / loop -> output
    m = re.fullmatch(r"(?:repeat|loop|run)\s+(\d+)\s+(?:times|x)\s+(?:print|display|say|show|output|echo)\s+(.+)", text, re.I)
    if m:
        program.add("repeat_print", count=int(m.group(1)), value=_literal(m.group(2))); return

    # While -> output
    m = re.fullmatch(r"while\s+("+NAME+r")\s+(greater than|less than|equal to|equals|not equal to)\s+(.+?)\s+(?:then\s+)?(?:print|display|say|show|output|echo)\s+(.+)", text, re.I)
    if m:
        ops={"greater than":">","less than":"<","equal to":"==","equals":"==","not equal to":"!="}
        program.add("while_print", name=m.group(1), op=ops[m.group(2).lower()], compare=_literal(m.group(3)), value=_literal(m.group(4))); return

    # Delay
    m = re.fullmatch(r"(?:wait|sleep|pause)\s+("+NUMBER+r")\s*(?:seconds?|secs?|s)?", text, re.I)
    if m:
        program.add("sleep", seconds=float(m.group(1))); return

    # Random number
    m = re.fullmatch(r"(?:generate|choose|pick|random(?:ly)?\s+(?:choose|generate|pick))\s+(?:a\s+)?random\s+(?:number\s+)?(?:from\s+)?(-?\d+)\s+(?:to|through)\s+(-?\d+)(?:\s+(?:and\s+)?store\s+(?:it\s+)?in\s+("+NAME+r"))?", text, re.I)
    if m:
        program.add("random", low=int(m.group(1)), high=int(m.group(2)), name=m.group(3) or "random_number"); return

    # Clear screen
    if re.fullmatch(r"(?:clear|clear\s+screen|cls)", text, re.I):
        program.add("clear"); return

    # SQL table
    m = re.fullmatch(r"(?:create|make)\s+(?:a\s+)?table\s+("+NAME+r")\s+(?:with|having)\s+(.+)", text, re.I)
    if m:
        columns=[]
        for item in m.group(2).split(","):
            parts=item.strip().split()
            if len(parts)<2: raise TranslationError("SQL columns need a name and type.")
            columns.append((parts[0]," ".join(parts[1:])))
        program.add("create_table", name=m.group(1), columns=columns); return

    raise TranslationError("Instruction not recognized. Try a supported command from README.md.")

def parse(text):
    text = text.strip()
    if not text:
        raise TranslationError("Input is empty.")
    p = Program()
    for command in _split_commands(text):
        _parse_one(command, p)
    return p
