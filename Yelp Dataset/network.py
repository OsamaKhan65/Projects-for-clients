# Import libraries
import pandas as pd
import json
import argparse

# Defining arguments for CLI
parser = argparse.ArgumentParser(description='Task #3')
parser.add_argument('addr', type=str, help='File path and name')
parser.add_argument('n', type=int, help='Minimum number of useful votes')
args = parser.parse_args()

if __name__ == '__main__':
    addr = args.addr
    n = args.n

# Importing json file as data frame
users = []
with open(addr) as fl:
    for i, line in enumerate(fl):
        users.append(json.loads(line))
fl.close()
business = pd.DataFrame(users)

# Filter dataframe rows with minimum entered # of useful votes
data = business.loc[business['useful'] >= n]

# Creating edge list with both friends having atleast n # of useful votes
a = list()
b = list()
for i in data["friends"].index:
    friends = data["friends"].loc[i].split(", ")
    if friends != ['None']:
        for friend in friends:
            temp = data.loc[data["user_id"]==friend]
            if temp.shape[0]!=0:
                if temp["useful"].item() >= n:
                    a.append(data["user_id"].loc[i])
                    b.append(friend)

# Removing duplicated entries
for i in range (len(a)):
    for j in range(i,len(a)-1):
        if (a[i]==b[j]) and (a[j]==b[i]):
            a.pop(j)
            b.pop(j)
for i in range (len(a)):
    for j in range(i,len(a)):
        if (a[i]==b[j]) and (a[j]==b[i]):
            a.pop(j)
            b.pop(j)

# Saving the output file
with open('Q3.out', 'w') as f:
    for i in range(len(a)):
        f.write(a[i])
        f. write(" ")
        f.write(b[i])
        f.write('\n')
f.close()