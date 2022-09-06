#!/venv/bin/python3.7.0

with open('q3mapped.txt', 'r') as f:
    json_obj = f.readlines()
f.close()

rids, d_ts, ufcs = [], [], []
for i in json_obj:
    rid, d_t, ufc = i[1:-2].split(', ')
    rids.append(rid)
    d_ts.append(int(d_t))
    ufcs.append(int(ufc))

ufcs, d_ts, rids = map(list,zip(*sorted(zip(ufcs, d_ts, rids),reverse=True)))

with open('q3reduced.txt', 'w') as f:
    for i in range(4415):
        line = rids[i]+"\t"+str(ufcs[i])+"\n"
        f.write(line)
f.close()
