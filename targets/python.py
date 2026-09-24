def _v(v):
    return repr(v)

def generate(p):
    out = []
    for o in p.operations:
        d = o.data
        if o.kind == "print":
            out.append(f"print({_v(d['value'])})")
        elif o.kind == "assign":
            out.append(f"{d['name']} = {_v(d['value'])}")
        elif o.kind == "if_print":
            out.append(f"if {d['name']} {d['op']} {_v(d['compare'])}:")
            out.append(f"    print({_v(d['value'])})")
        elif o.kind == "repeat_print":
            out.append(f"for _ in range({d['count']}):")
            out.append(f"    print({_v(d['value'])})")
        elif o.kind == "create_table":
            cols = ", ".join(f"{n} {t}" for n, t in d["columns"])
            out.append(f"# SQL: CREATE TABLE {d['name']} ({cols});")
    return "\n".join(out) + "\n"
