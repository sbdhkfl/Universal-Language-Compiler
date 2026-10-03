def q(v): return '"'+v.replace('\\','\\\\').replace('"','\\\"')+'"' if isinstance(v,str) else str(v)
def generate(p):
    out=['using System;','using System.Threading;','using System;','','class Program {','    static void Main() {']
    for o in p.operations:
        d=o.data
        if o.kind=='comment': out.append('        // '+d['value'])
        elif o.kind=='print': out.append(f'        Console.WriteLine({q(d["value"])});')
        elif o.kind=='assign': out.append(f'        var {d["name"]} = {q(d["value"])};')
        elif o.kind=='input': out += [f'        Console.Write({q(d["prompt"])});',f'        var {d["name"]} = Console.ReadLine();']
        elif o.kind=='math': out.append(f'        {d["name"]} = {d["name"]} {d["op"]} {q(d["value"])};')
        elif o.kind=='if_print': out += [f'        if ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'            Console.WriteLine({q(d["value"])});','        }']
        elif o.kind=='repeat_print': out += [f'        for (int i=0; i<{d["count"]}; i++) {{',f'            Console.WriteLine({q(d["value"])});','        }']
        elif o.kind=='while_print': out += [f'        while ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'            Console.WriteLine({q(d["value"])});','        }']
        elif o.kind=='sleep': out.append(f'        Thread.Sleep({int(d["seconds"]*1000)});')
        elif o.kind=='random': out.append(f'        int {d["name"]} = new Random().Next({d["low"]}, {d["high"]+1});')
        elif o.kind=='clear': out.append('        Console.Clear();')
        elif o.kind=='create_table': out.append('        // SQL CREATE TABLE '+d['name'])
    out += ['    }','}']
    return '\n'.join(out)+'\n'
