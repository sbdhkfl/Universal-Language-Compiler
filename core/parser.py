import re
from .errors import TranslationError
from .ir import Program

NUMBER=r"-?\d+(?:\.\d+)?"
def _literal(value):
    value=value.strip().rstrip(".")
    if re.fullmatch(NUMBER,value): return float(value) if "." in value else int(value)
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")): return value[1:-1]
    return value

def parse(text):
    text=text.strip()
    if not text: raise TranslationError("Input is empty.")
    p=Program()
    m=re.fullmatch(r"(?:print|display|say)\s+(.+)",text,re.I)
    if m: p.add("print",value=_literal(m.group(1))); return p
    m=re.fullmatch(r"(?:create|make|set)\s+(?:a\s+)?variable\s+(?:called\s+)?([A-Za-z_]\w*)\s+(?:equal\s+to|=|equal\s+)(.+)",text,re.I)
    if m: p.add("assign",name=m.group(1),value=_literal(m.group(2))); return p
    m=re.fullmatch(r"if\s+([A-Za-z_]\w*)\s+(?:is\s+)?(greater than|less than|equal to|not equal to)\s+(.+?)\s+(?:then\s+)?(?:print|display|say)\s+(.+)",text,re.I)
    if m:
        ops={"greater than":">","less than":"<","equal to":"==","not equal to":"!="}
        p.add("if_print",name=m.group(1),op=ops[m.group(2).lower()],compare=_literal(m.group(3)),value=_literal(m.group(4))); return p
    m=re.fullmatch(r"(?:repeat|loop)\s+(\d+)\s+times\s+(?:print|display|say)\s+(.+)",text,re.I)
    if m: p.add("repeat_print",count=int(m.group(1)),value=_literal(m.group(2))); return p
    m=re.fullmatch(r"create\s+(?:a\s+)?table\s+(\w+)\s+with\s+(.+)",text,re.I)
    if m:
        columns=[]
        for item in m.group(2).split(','):
            parts=item.strip().split()
            if len(parts)<2: raise TranslationError("SQL columns need a name and type.")
            columns.append((parts[0]," ".join(parts[1:])))
        p.add("create_table",name=m.group(1),columns=columns); return p
    raise TranslationError("Instruction not recognized. See README.md for supported patterns.")
