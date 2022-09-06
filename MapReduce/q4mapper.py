#!/venv/bin/python3.7.0

with open('/home/osama/Documents/data/yelp_academic_dataset_business.json', 'r') as f:
    json_obj = f.readlines()
json_obj = [(obj.rstrip()).lstrip()[:-1] for obj in json_obj[1:-1]]
f.close()

with open('q4mapped.txt', 'w') as f:
    for i in range(len(json_obj)):
        x = json_obj[i]
        bid = x[x.find('"business_id":')+15:x.find('","name"')]
        bnm = x[x.find('"name":') + 8:x.find('","address"')]
        tup = "("+bid+", "+bnm+")\n"
        f.write(tup)
f.close()
