def q(v): return '"'+v.replace('\\','\\\\').replace('"','\\"')+'"' if isinstance(v,str) else str(v)
def generate(p):
    out=['fn main() {']
    for o in p.operations:
        d=o.data
        if o.kind=='print': out.append(f'    println!({q(d["value"])});')
        elif o.kind=='assign': out.append(f'    let {d["name"]} = {q(d["value"])};')
        elif o.kind=='if_print': out += [f'    if {d["name"]} {d["op"]} {q(d["compare"])} {{',f'        println!({q(d["value"])});','    }']
        elif o.kind=='repeat_print': out += [f'    for _ in 0..{d["count"]} {{',f'        println!({q(d["value"])});','    }']
    out.append('}')
    return '\n'.join(out)+'\n'
