from .parser import parse
from .validator import validate
from targets import get_target

def translate(text: str, target: str) -> str:
    program = parse(text)
    validate(program)
    return get_target(target).generate(program)
