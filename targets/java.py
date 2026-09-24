def _v(v):
    if isinstance(v, str): return '"' + v.replace('\\','\\\\').replace('"','\\"') + '"'
    return str(v).lower() if isinstance(v,bool) else str(v)

def generate(p):
    out=["public class Main {","    public static void main(String[] args) {"]
    for o in p.operations:
        d=o.data
        if o.kind=="print": out.append(f"        System.out.println({_v(d['value'])});")
        elif o.kind=="assign": out.append(f"        var {d['name']} = {_v(d['value'])};")
        elif o.kind=="if_print": out += [f"        if ({d['name']} {d['op']} {_v(d['compare'])}) {{",f"            System.out.println({_v(d['value'])});","        }"]
        elif o.kind=="repeat_print": out += [f"        for (int i = 0; i < {d['count']}; i++) {{",f"            System.out.println({_v(d['value'])});","        }"]
    out += ["    }","}"]
    return "\n".join(out)+"\n"
