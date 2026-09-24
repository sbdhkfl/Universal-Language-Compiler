def q(v): return '"'+v.replace('\\','\\\\').replace('"','\\"')+'"' if isinstance(v,str) else str(v)
def generate(p):
    out=['using System;','','class Program {','    static void Main() {']
    for o in p.operations:
        d=o.data
        if o.kind=='print': out.append(f'        Console.WriteLine({q(d["value"])});')
        elif o.kind=='assign': out.append(f'        var {d["name"]} = {q(d["value"])};')
        elif o.kind=='if_print': out += [f'        if ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'            Console.WriteLine({q(d["value"])});','        }']
        elif o.kind=='repeat_print': out += [f'        for (int i=0; i<{d["count"]}; i++) {{',f'            Console.WriteLine({q(d["value"])});','        }']
    out += ['    }','}']
    return '\n'.join(out)+'\n'
