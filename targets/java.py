def q(v): return '"'+v.replace('\\','\\\\').replace('"','\\\"')+'"' if isinstance(v,str) else str(v)
def generate(p):
    out=['import java.util.*;','public class Main {','    public static void main(String[] args) {']
    for o in p.operations:
        d=o.data
        if o.kind=='comment': out.append('        // '+d['value'])
        elif o.kind=='print': out.append(f'        System.out.println({q(d["value"])});')
        elif o.kind=='assign': out.append(f'        var {d["name"]} = {q(d["value"])};')
        elif o.kind=='input': out += ['        Scanner scanner = new Scanner(System.in);',f'        System.out.print({q(d["prompt"])});',f'        String {d["name"]} = scanner.nextLine();']
        elif o.kind=='math': out.append(f'        {d["name"]} = {d["name"]} {d["op"]} {q(d["value"])};')
        elif o.kind=='if_print': out += [f'        if ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'            System.out.println({q(d["value"])});','        }']
        elif o.kind=='repeat_print': out += [f'        for (int i=0; i<{d["count"]}; i++) {{',f'            System.out.println({q(d["value"])});','        }']
        elif o.kind=='while_print': out += [f'        while ({d["name"]} {d["op"]} {q(d["compare"])}) {{',f'            System.out.println({q(d["value"])});','        }']
        elif o.kind=='sleep': out.append(f'        try {{ Thread.sleep({int(d["seconds"]*1000)}); }} catch (InterruptedException ignored) {{}}')
        elif o.kind=='random': out.append(f'        int {d["name"]} = new Random().nextInt({d["high"]-d["low"]+1}) + {d["low"]};')
        elif o.kind=='clear': out.append('        System.out.print("\\033[2J\\033[H");')
        elif o.kind=='create_table': out.append('        // SQL CREATE TABLE '+d['name'])
    out += ['    }','}']
    return '\n'.join(out)+'\n'
