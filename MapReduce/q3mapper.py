#!/venv/bin/python3.7.0

with open('/home/osama/Documents/data/yelp_academic_dataset_review.json', 'r') as f:
    json_obj = f.readlines()
json_obj = [(obj.rstrip()).lstrip()[:-1] for obj in json_obj[1:-1]]
f.close()

with open('q3mapped.txt', 'w') as f:
    for i in json_obj:
        rid = i[i.find('"review_id":"') + 13:i.find('","user_id":')]
        ufc = int(i[i.find('"useful":') + 9:i.find(',"funny":')])
        ufc+= int(i[i.find('"funny":') + 8:i.find(',"cool":')])
        ufc+= int(i[i.find('"cool":') + 7:i.find(',"text":')])
        d_t = i[i.find('"date":"') + 8:-3]
        d_t = d_t[:4]+d_t[5:7]+d_t[8:10]+d_t[11:13]+d_t[14:16]+d_t[17:]
        line = "(" + rid + ", " + d_t + ", " + str(ufc) + ")\n"
        f.write(line)
f.close()
