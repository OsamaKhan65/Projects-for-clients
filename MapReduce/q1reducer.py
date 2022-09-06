#!/venv/bin/python3.7.0

with open('q1mapped.txt', 'r') as f:
    json_obj = f.readlines()
f.close()

red = dict()
for i in range(len(json_obj)):
    x = json_obj[i][1:-2]
    cat, ind = x.split(", ")
    if cat in red.keys():
        red[cat].append(ind)
    else:
        red[cat] = [ind]

with open('q1reduced.txt', 'w') as f:
    for n in red.keys():
        tup = n+"\t"+str(red[n])+"\n"
        f.write(tup)
f.close()
