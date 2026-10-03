def q(v):
    if isinstance(v,str): return '"'+v.replace('\\','\\\\').replace('"','\\\"')+'"'
    return str(v).lower() if isinstance(v,bool) else str(v)
def generate(p):
    out=[]
    for o in p.operations:
        d=o.data
        if o.kind=='comment': out.append('// '+d['value'])
        elif o.kind=='print': out.append(f'console.log({q(d["value"])});')
        elif o.kind=='assign': out.append(f'let {d["name"]} = {q(d["value"])};')
        elif o.kind=='input': out.append(f'let {d["name"]} = prompt({q(d["prompt"])});')
        elif o.kind=='math': out.append(f'{d["name"]} = {d["name"]} {d["op"]} {q(d["value"])};')
        elif o.kind=='if_print': out += [f'if ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'    console.log({q(d["value"])});','}']
        elif o.kind=='repeat_print': out += [f'for (let i=0; i<{d["count"]}; i++) {{',f'    console.log({q(d["value"])});','}']
        elif o.kind=='while_print': out += [f'while ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'    console.log({q(d["value"])});','}']
        elif o.kind=='sleep': out.append(f'await new Promise(r => setTimeout(r, {int(d["seconds"]*1000)}));')
        elif o.kind=='random': out.append(f'let {d["name"]} = Math.floor(Math.random()*({d["high"]}-{d["low"]+1}))+{d["low"]};')
        elif o.kind=='clear': out.append('console.clear();')
        elif o.kind=='create_table': out.append('// SQL CREATE TABLE '+d['name'])
    return '\n'.join(out)+'\n'
