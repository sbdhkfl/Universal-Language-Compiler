from .errors import TranslationError
from .ir import Program

SUPPORTED = {"print", "assign", "if_print", "repeat_print", "create_table"}

def validate(program: Program) -> None:
    if not program.operations:
        raise TranslationError("Program contains no operations.")
    for op in program.operations:
        if op.kind not in SUPPORTED:
            raise TranslationError(f"Unsupported IR operation: {op.kind}")
        if op.kind == "assign" and not op.data["name"].isidentifier():
            raise TranslationError("Invalid variable name.")
