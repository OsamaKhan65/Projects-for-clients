# Import libraries
import pandas as pd
import json
import argparse

# Defining arguments for CLI
parser = argparse.ArgumentParser(description='Task #1')
parser.add_argument('addr', type=str, help='File path and name')
parser.add_argument('city', type=str, help='City name')
parser.add_argument('state', type=str, help='State Name (ST)')
args = parser.parse_args()

if __name__ == '__main__':
    city = args.city
    state = args.state
    addr = args.addr

# Importing json file as data frame
users = []
with open(addr) as fl:
    for i, line in enumerate(fl):
        users.append(json.loads(line))
fl.close()
business = pd.DataFrame(users)

# Filter dataframe rows with entered city and state
data = business.loc[(business['city']==city) & (business['state']==state)]

# Calculating # of restaurants, total stars and review counts of restaurants
c, s, r = 0, 0, 0
for i in data.index:
    if str(data['categories'].loc[i]).find('Restaurants') != -1:
        c+=1
        s+=data['stars'].loc[i]
        r+=data['review_count'].loc[i]

# Saving the values to be printed in a list
lines = [data.shape[0],                              # number of businesses in the city, ST
         round(data['stars'].mean()*100)/100,        # average number of stars of businesses in the city, ST
         c,                                          # number of restaurants in the city, ST
         round(s*100/c)/100,                         # average number of stars of restaurants in the city, ST
         round(data['review_count'].mean()*100)/100, # average number of reviews for all businesses in the city, ST
         round(r*100/c)/100]                         # average number of reviews for restaurants in the city, ST

# Saving the output file
with open('Q1.out', 'w') as f:
    for line in lines:
        f.write(str(line))
        f.write('\n')
f.close()