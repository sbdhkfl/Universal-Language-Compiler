def q(v): return '"'+v.replace('"','""')+'"' if isinstance(v,str) else str(v)
def generate(p):
    out=['Module Program','    Sub Main()']
    for o in p.operations:
        d=o.data
        if o.kind=='print': out.append(f'        Console.WriteLine({q(d["value"])})')
        elif o.kind=='assign': out.append(f'        Dim {d["name"]} = {q(d["value"])}')
        elif o.kind=='if_print': out += [f'        If {d["name"]} {d["op"]} {q(d["compare"])} Then',f'            Console.WriteLine({q(d["value"])})','        End If']
        elif o.kind=='repeat_print': out += [f'        For i As Integer = 0 To {d["count"]-1}',f'            Console.WriteLine({q(d["value"])})','        Next']
    out += ['    End Sub','End Module']
    return '\n'.join(out)+'\n'
