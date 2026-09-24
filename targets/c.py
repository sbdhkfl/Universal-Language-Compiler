def q(v):
    if isinstance(v,str): return '"'+v.replace('\\','\\\\').replace('"','\\"')+'"'
    return str(v)
def generate(p):
    out=['#include <stdio.h>','','int main(void) {']
    for o in p.operations:
        d=o.data
        if o.kind=='print': out.append(f'    printf("%s\\n", {q(d["value"])});')
        elif o.kind=='assign': out.append(f'    double {d["name"]} = {q(d["value"])};')
        elif o.kind=='if_print': out += [f'    if ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'        printf("%s\\n", {q(d["value"])});','    }']
        elif o.kind=='repeat_print': out += [f'    for (int i=0; i<{d["count"]}; i++) {{',f'        printf("%s\\n", {q(d["value"])});','    }']
    out += ['    return 0;','}']
    return '\n'.join(out)+'\n'
