def _v(v):
    if isinstance(v,str): return '"' + v.replace('"','""') + '"'
    return str(v)

def generate(p):
    out=["Module Program","    Sub Main()"]
    for o in p.operations:
        d=o.data
        if o.kind=="print": out.append(f"        Console.WriteLine({_v(d['value'])})")
        elif o.kind=="assign": out.append(f"        Dim {d['name']} = {_v(d['value'])}")
        elif o.kind=="if_print": out += [f"        If {d['name']} {d['op']} {_v(d['compare'])} Then",f"            Console.WriteLine({_v(d['value'])})","        End If"]
        elif o.kind=="repeat_print": out += [f"        For i As Integer = 0 To {d['count']-1}",f"            Console.WriteLine({_v(d['value'])})","        Next"]
    out += ["    End Sub","End Module"]
    return "\n".join(out)+"\n"
