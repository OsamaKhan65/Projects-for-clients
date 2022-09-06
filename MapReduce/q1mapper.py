#!/venv/bin/python3.7.0

with open('/home/osama/Documents/data/yelp_academic_dataset_business.json', 'r') as f:
    json_obj = f.readlines()
json_obj = [(obj.rstrip()).lstrip()[:-1] for obj in json_obj[1:-1]]
f.close()

with open('q1mapped.txt', 'w') as f:
    for i in range(len(json_obj)):
        x = json_obj[i]
        if (x.find('Saturday')+1) or (x.find('Sunday')+1):
            if x.find('"categories":null')<0:
                cat = x[x.find('"categories":')+14:x.find('","hours"')]
                cat = cat.split(", ")
                ind = x[x.find('"business_id":')+15:x.find('","name"')]
                for n in cat:
                    tup = "("+n+", "+ind+")\n"
                    f.write(tup)
f.close()
