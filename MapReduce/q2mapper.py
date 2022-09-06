#!/venv/bin/python3.7.0

with open('/home/osama/Documents/data/yelp_academic_dataset_user.json', 'r') as f:
    json_obj = f.readlines()
json_obj = [(obj.rstrip()).lstrip()[:-1] for obj in json_obj[1:-1]]
f.close()

with open('q2mapped.txt', 'w') as f:
    for i in json_obj:
        m = i[i.find('"yelping_since":"') + 22:i.find('","useful":') - 12]
        line = "("+m+", 1)\n"
        f.write(line)
f.close()
