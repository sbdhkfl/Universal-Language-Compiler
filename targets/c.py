def q(v):
    if isinstance(v,str): return '"'+v.replace('\\','\\\\').replace('"','\\\"')+'"'
    return str(v)
def generate(p):
    out=['#include <stdio.h>','#include <stdlib.h>','#include <time.h>','#include <unistd.h>','','int main(void) {']
    for o in p.operations:
        d=o.data
        if o.kind=='comment': out.append('    /* '+d['value']+' */')
        elif o.kind=='print': out.append(f'    printf("%s\\n", {q(d["value"])});')
        elif o.kind=='assign': out.append(f'    double {d["name"]} = {q(d["value"])};')
        elif o.kind=='input': out += [f'    char {d["name"]}[256];',f'    printf("%s", {q(d["prompt"])});',f'    fgets({d["name"]}, sizeof({d["name"]}), stdin);']
        elif o.kind=='math': out.append(f'    {d["name"]} = {d["name"]} {d["op"]} {q(d["value"])};')
        elif o.kind=='if_print': out += [f'    if ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'        printf("%s\\n", {q(d["value"])});','    }']
        elif o.kind=='repeat_print': out += [f'    for (int i=0; i<{d["count"]}; i++) {{',f'        printf("%s\\n", {q(d["value"])});','    }']
        elif o.kind=='while_print': out += [f'    while ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'        printf("%s\\n", {q(d["value"])});','    }']
        elif o.kind=='sleep': out.append(f'    sleep((unsigned int){d["seconds"]});')
        elif o.kind=='random': out.append(f'    int {d["name"]} = rand() % ({d["high"]}-{d["low"]+1}) + {d["low"]};')
        elif o.kind=='clear': out.append('    printf("\\033[2J\\033[H");')
        elif o.kind=='create_table': out.append('    /* SQL CREATE TABLE '+d['name']+' */')
    out += ['    return 0;','}']
    return '\n'.join(out)+'\n'
