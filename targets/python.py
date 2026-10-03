import random, time
def q(v): return repr(v)
def generate(p):
    out=[]
    for o in p.operations:
        d=o.data
        if o.kind=="comment": out.append(f"# {d['value']}")
        elif o.kind=="print": out.append(f"print({q(d['value'])})")
        elif o.kind=="assign": out.append(f"{d['name']} = {q(d['value'])}")
        elif o.kind=="input": out.append(f"{d['name']} = input({q(d['prompt'])})")
        elif o.kind=="math": out.append(f"{d['name']} = {d['name']} {d['op']} {q(d['value'])}")
        elif o.kind=="if_print": out += [f"if {d['name']} {d['op']} {q(d['compare'])}:",f"    print({q(d['value'])})"]
        elif o.kind=="repeat_print": out += [f"for _ in range({d['count']}):",f"    print({q(d['value'])})"]
        elif o.kind=="while_print": out += [f"while {d['name']} {d['op']} {q(d['compare'])}:",f"    print({q(d['value'])})"]
        elif o.kind=="sleep": out.append(f"time.sleep({d['seconds']})")
        elif o.kind=="random": out.append(f"{d['name']} = random.randint({d['low']}, {d['high']})")
        elif o.kind=="clear": out.append("print('\\033[2J\\033[H', end='')")
        elif o.kind=="create_table": out.append("# SQL: CREATE TABLE " + d["name"] + ";")
    return "\n".join(out)+"\n"
