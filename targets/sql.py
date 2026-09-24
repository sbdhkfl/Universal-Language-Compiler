def _v(v):
    return "'" + str(v).replace("'","''") + "'"

def generate(p):
    out=[]
    for o in p.operations:
        d=o.data
        if o.kind=="create_table":
            cols=", ".join(f"{n} {t}" for n,t in d["columns"])
            out.append(f"CREATE TABLE {d['name']} ({cols});")
        elif o.kind=="print":
            out.append(f"SELECT {_v(d['value'])} AS message;")
        else:
            out.append(f"-- Operation {o.kind} is not a portable SQL operation.")
    return "\n".join(out)+"\n"
