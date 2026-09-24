def _v(v):
    if isinstance(v,str): return '"' + v.replace('\\','\\\\').replace('"','\\"') + '"'
    if isinstance(v,bool): return str(v).lower()
    return str(v)

def generate(p):
    out=[]
    for o in p.operations:
        d=o.data
        if o.kind=="print": out.append(f"console.log({_v(d['value'])});")
        elif o.kind=="assign": out.append(f"let {d['name']} = {_v(d['value'])};")
        elif o.kind=="if_print": out += [f"if ({d['name']} {d['op']} {_v(d['compare'])}) {{",f"    console.log({_v(d['value'])});","}"]
        elif o.kind=="repeat_print": out += [f"for (let i = 0; i < {d['count']}; i++) {{",f"    console.log({_v(d['value'])});","}"]
    return "\n".join(out)+"\n"
