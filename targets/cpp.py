def _v(v):
    if isinstance(v, str): return '"' + v.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return str(v)

def generate(p):
    out=["#include <iostream>","","int main() {"]
    for o in p.operations:
        d=o.data
        if o.kind=="print": out.append(f"    std::cout << {_v(d['value'])} << std::endl;")
        elif o.kind=="assign": out.append(f"    auto {d['name']} = {_v(d['value'])};")
        elif o.kind=="if_print": out += [f"    if ({d['name']} {d['op']} {_v(d['compare'])}) {{",f"        std::cout << {_v(d['value'])} << std::endl;","    }"]
        elif o.kind=="repeat_print": out += [f"    for (int i = 0; i < {d['count']}; ++i) {{",f"        std::cout << {_v(d['value'])} << std::endl;","    }"]
        elif o.kind=="create_table": out.append("    // SQL table creation belongs in a database.")
    out += ["    return 0;","}"]
    return "\n".join(out)+"\n"
