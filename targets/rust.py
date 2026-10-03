def q(v): return '"'+v.replace('\\','\\\\').replace('"','\\\"')+'"' if isinstance(v,str) else str(v)
def generate(p):
    out=['use std::io::{self, Write};','use std::{thread, time};','','fn main() {']
    for o in p.operations:
        d=o.data
        if o.kind=='comment': out.append('    // '+d['value'])
        elif o.kind=='print': out.append(f'    println!({q(d["value"])});')
        elif o.kind=='assign': out.append(f'    let mut {d["name"]} = {q(d["value"])};')
        elif o.kind=='input': out += [f'    print!({q(d["prompt"])}); io::stdout().flush().unwrap();',f'    let mut {d["name"]} = String::new(); io::stdin().read_line(&mut {d["name"]}).unwrap();']
        elif o.kind=='math': out.append(f'    {d["name"]} = {d["name"]} {d["op"]} {q(d["value"])};')
        elif o.kind=='if_print': out += [f'    if {d["name"]} {d["op"]} {q(d["compare"])} {{',f'        println!({q(d["value"])});','    }']
        elif o.kind=='repeat_print': out += [f'    for _ in 0..{d["count"]} {{',f'        println!({q(d["value"])});','    }']
        elif o.kind=='while_print': out += [f'    while {d["name"]} {d["op"]} {q(d["compare"])} {{',f'        println!({q(d["value"])});','    }']
        elif o.kind=='sleep': out.append(f'    thread::sleep(time::Duration::from_millis({int(d["seconds"]*1000)}));')
        elif o.kind=='random': out.append(f'    let {d["name"]} = {d["low"]}; // add rand crate for true randomness')
        elif o.kind=='clear': out.append('    print!("\\x1b[2J\\x1b[H");')
        elif o.kind=='create_table': out.append('    // SQL CREATE TABLE '+d['name'])
    out.append('}')
    return '\n'.join(out)+'\n'
