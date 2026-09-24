def q(v): return '"'+v.replace('\\','\\\\').replace('"','\\"')+'"' if isinstance(v,str) else str(v)
def generate(p):
    out=[]
    for o in p.operations:
        d=o.data
        if o.kind=='print': out.append(f'print({q(d["value"])})')
        elif o.kind=='assign': out.append(f'{d["name"]} <- {q(d["value"])}')
        elif o.kind=='if_print': out += [f'if ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'  print({q(d["value"])})','}']
        elif o.kind=='repeat_print': out += [f'for (i in 1:{d["count"]}) {{',f'  print({q(d["value"])})','}']
    return '\n'.join(out)+'\n'
