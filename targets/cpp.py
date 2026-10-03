def q(v): return '"'+v.replace('\\','\\\\').replace('"','\\\"')+'"' if isinstance(v,str) else str(v)
def generate(p):
    out=['#include <iostream>','#include <thread>','#include <chrono>','#include <random>','','int main() {']
    for o in p.operations:
        d=o.data
        if o.kind=='comment': out.append('    // '+d['value'])
        elif o.kind=='print': out.append(f'    std::cout << {q(d["value"])} << std::endl;')
        elif o.kind=='assign': out.append(f'    auto {d["name"]} = {q(d["value"])};')
        elif o.kind=='input': out += [f'    std::string {d["name"]};',f'    std::cout << {q(d["prompt"])};',f'    std::getline(std::cin, {d["name"]});']
        elif o.kind=='math': out.append(f'    {d["name"]} = {d["name"]} {d["op"]} {q(d["value"])};')
        elif o.kind=='if_print': out += [f'    if ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'        std::cout << {q(d["value"])} << std::endl;','    }']
        elif o.kind=='repeat_print': out += [f'    for (int i=0; i<{d["count"]}; ++i) {{',f'        std::cout << {q(d["value"])} << std::endl;','    }']
        elif o.kind=='while_print': out += [f'    while ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'        std::cout << {q(d["value"])} << std::endl;','    }']
        elif o.kind=='sleep': out.append(f'    std::this_thread::sleep_for(std::chrono::milliseconds({int(d["seconds"]*1000)}));')
        elif o.kind=='random': out.append(f'    int {d["name"]} = std::rand() % ({d["high"]}-{d["low"]+1}) + {d["low"]};')
        elif o.kind=='clear': out.append('    std::cout << "\\033[2J\\033[H";')
        elif o.kind=='create_table': out.append('    // SQL CREATE TABLE '+d['name'])
    out += ['    return 0;','}']
    return '\n'.join(out)+'\n'
