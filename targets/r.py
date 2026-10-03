def q(v): return '"'+v.replace('\\','\\\\').replace('"','\\\"')+'"' if isinstance(v,str) else str(v)
def generate(p):
    out=['set.seed(NULL)']
    for o in p.operations:
        d=o.data
        if o.kind=='comment': out.append('# '+d['value'])
        elif o.kind=='print': out.append(f'print({q(d["value"])})')
        elif o.kind=='assign': out.append(f'{d["name"]} <- {q(d["value"])}')
        elif o.kind=='input': out.append(f'{d["name"]} <- readline({q(d["prompt"])})')
        elif o.kind=='math': out.append(f'{d["name"]} <- {d["name"]} {d["op"]} {q(d["value"])}')
        elif o.kind=='if_print': out += [f'if ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'  print({q(d["value"])})','}']
        elif o.kind=='repeat_print': out += [f'for (i in 1:{d["count"]}) {{',f'  print({q(d["value"])})','}']
        elif o.kind=='while_print': out += [f'while ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'  print({q(d["value"])})','}']
        elif o.kind=='sleep': out.append(f'Sys.sleep({d["seconds"]})')
        elif o.kind=='random': out.append(f'{d["name"]} <- sample({d["low"]}:{d["high"]}, 1)')
        elif o.kind=='clear': out.append('cat("\\033[2J\\033[H")')
        elif o.kind=='create_table': out.append('# SQL CREATE TABLE '+d['name'])
    return '\n'.join(out)+'\n'
