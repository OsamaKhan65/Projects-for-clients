#!/venv/bin/python3.7.0

with open('q2mapped.txt', 'r') as f:
    json_obj = f.readlines()
f.close()

count = {'01':0, '02':0, '03':0, '04':0,
         '05':0, '06':0, '07':0, '08':0,
         '09':0, '10':0, '11':0, '12':0}
for i in json_obj:
    count[i[1:3]] += 1

with open('q2reduced.txt', 'w') as f:
    for i in count:
        freq = str(round(100*count[i]/len(json_obj), 2))
        line = str(int(i))+"\t"+freq+"%\n"
        f.write(line)
f.close()
