def q(v): return '"'+v.replace('\\','\\\\').replace('"','\\"')+'"' if isinstance(v,str) else str(v)
def generate(p):
    out=['#include <iostream>','','int main() {']
    for o in p.operations:
        d=o.data
        if o.kind=='print': out.append(f'    std::cout << {q(d["value"])} << std::endl;')
        elif o.kind=='assign': out.append(f'    auto {d["name"]} = {q(d["value"])};')
        elif o.kind=='if_print': out += [f'    if ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'        std::cout << {q(d["value"])} << std::endl;','    }']
        elif o.kind=='repeat_print': out += [f'    for (int i=0; i<{d["count"]}; ++i) {{',f'        std::cout << {q(d["value"])} << std::endl;','    }']
    out += ['    return 0;','}']
    return '\n'.join(out)+'\n'
