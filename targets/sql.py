def q(v): return "'"+str(v).replace("'","''")+"'"
def generate(p):
    out=[]
    for o in p.operations:
        d=o.data
        if o.kind=='create_table': out.append(f'CREATE TABLE {d["name"]} ('+', '.join(f'{n} {t}' for n,t in d['columns'])+');')
        elif o.kind=='print': out.append(f'SELECT {q(d["value"])} AS message;')
        else: out.append(f'-- Operation {o.kind} is not a portable SQL operation.')
    return '\n'.join(out)+'\n'
