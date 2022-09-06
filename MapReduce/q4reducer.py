#!/venv/bin/python3.7.0

import random

with open('q4mapped.txt', 'r') as f:
    json_obj = f.readlines()
f.close()

with open('/home/osama/Documents/data/yelp_academic_dataset_checkin.json', 'r') as f:
    check_in = f.readlines()
f.close()

char = ['_', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
uids = []

with open('q4reduced.txt', 'w') as f:
    for ind in range(len(check_in)):
        check = check_in[ind]
        bid = check[check.find('"business_id":')+15:check.find('","date"')]
        for i in json_obj:
            if i.find(bid)>=0:
             break
        bnm = i[25:-2]

        dates = check[check.find('"date":"')+8:-3]
        dates = dates.split(", ")

        for date in dates:
            uid = ''
            while uid=='' or uid in uids:
                uid = ''
                for i in range(22):
                    c = random.choice(char)
                    uid += c
            uids.append(uid)
            line = uid+"\t"+date+"\t"+bnm+"\n"
            f.write(line)
f.close()
