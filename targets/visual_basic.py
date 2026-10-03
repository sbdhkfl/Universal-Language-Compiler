def q(v): return '"'+v.replace('"','""')+'"' if isinstance(v,str) else str(v)
def generate(p):
    out=['Imports System','Imports System.Threading','Module Program','    Sub Main()']
    for o in p.operations:
        d=o.data
        if o.kind=='comment': out.append("        ' "+d['value'])
        elif o.kind=='print': out.append(f'        Console.WriteLine({q(d["value"])})')
        elif o.kind=='assign': out.append(f'        Dim {d["name"]} = {q(d["value"])}')
        elif o.kind=='input': out += [f'        Console.Write({q(d["prompt"])})',f'        Dim {d["name"]} = Console.ReadLine()']
        elif o.kind=='math': out.append(f'        {d["name"]} = {d["name"]} {d["op"]} {q(d["value"])}')
        elif o.kind=='if_print': out += [f'        If {d["name"]} {d["op"]} {q(d["compare"])} Then',f'            Console.WriteLine({q(d["value"])})','        End If']
        elif o.kind=='repeat_print': out += [f'        For i As Integer = 0 To {d["count"]-1}',f'            Console.WriteLine({q(d["value"])})','        Next']
        elif o.kind=='while_print': out += [f'        While {d["name"]} {d["op"]} {q(d["compare"])}',f'            Console.WriteLine({q(d["value"])})','        End While']
        elif o.kind=='sleep': out.append(f'        Thread.Sleep({int(d["seconds"]*1000)})')
        elif o.kind=='random': out.append(f'        Dim {d["name"]} = New Random().Next({d["low"]}, {d["high"]+1})')
        elif o.kind=='clear': out.append('        Console.Clear()')
        elif o.kind=='create_table': out.append("        ' SQL CREATE TABLE "+d['name'])
    out += ['    End Sub','End Module']
    return '\n'.join(out)+'\n'
