def q(v):
    if isinstance(v,str): return '"'+v.replace('\\','\\\\').replace('"','\\"')+'"'
    return str(v).lower() if isinstance(v,bool) else str(v)
def generate(p):
    out=[]
    for o in p.operations:
        d=o.data
        if o.kind=='print': out.append(f'console.log({q(d["value"])});')
        elif o.kind=='assign': out.append(f'let {d["name"]} = {q(d["value"])};')
        elif o.kind=='if_print': out += [f'if ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'    console.log({q(d["value"])});','}']
        elif o.kind=='repeat_print': out += [f'for (let i=0; i<{d["count"]}; i++) {{',f'    console.log({q(d["value"])});','}']
    return '\n'.join(out)+'\n'
