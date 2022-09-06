# Import libraries
import pandas as pd
import json
import argparse
import matplotlib.pyplot as plt

# Defining arguments for CLI
parser = argparse.ArgumentParser(description='Task #2')
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

# Saving row #s of restaurants in a list
res = list()
for i in data.index:
    if str(data['categories'].loc[i]).find('Restaurants') != -1:
        res.append(i)

# Saving types of restaurants in a list
x = list()
for i in res:
    cat = data["categories"].loc[i].split(", ")
    for j in cat:
        x.append(j)

# Saving names of types of restaurants (Done Manually)
country = ['Thai', 'Canadian (New)', 'American (New)', 'Chinese',
           'Asian Fusion', 'American (Traditional)', 'Filipino',
           'Italian', 'Mexican', 'Japanese', 'Vietnamese', 'German',
           'Modern European', 'Lebanese', 'Mediterranean',
           'Middle Eastern', 'French', 'Taiwanese', 'Latin American',
           'British', 'Pakistani', 'Indian', 'Greek', 'Himalayan/Nepalese',
           'Singaporean', 'Indonesian', 'Moroccan', 'Korean', 'Southern',
           'Hawaiian', 'Irish', 'Afghan', 'Venezuelan', 'Malaysian',
           'Austrian', 'Belgian', 'Hungarian', 'Ukrainian', 'Cuban',
           'Peruvian', 'Cambodian', 'Caribbean', 'African', 'Shanghainese',
           'Mongolian', 'Portuguese', 'Brazilian', 'Ethiopian',
           'South African', 'Spanish', 'Cantonese', 'Colombian',
           'Salvadoran', 'Persian/Iranian', 'Bulgarian', 'Turkish',
           'Australian', 'Polish', 'Syrian', 'Scandinavian', 'Arabian',
           'Russian', 'Burmese', 'Sri Lankan', 'Egyptian', 'Bangladeshi',
           'Cajun/Creole', 'Basque', 'Szechuan', 'Pan Asian', 'Laotian']

# Calculating the #, review count and avg review count of restaurants based on type
x = list()
r = list()
t = list()
for j in country:
    count, review = 0,0
    for i in res:
        if str(data['categories'].loc[i]).find(j) != -1:
            count+=1
            review+=data['review_count'].loc[i]
    x.append(count)
    r.append(review)
    if count > 0:
        t.append(round((review / count) * 100) / 100)
    else:
        t.append(0)

# Saving the calculated values as dataframe
frequency_table = pd.DataFrame(data=country, columns=["Country"])
frequency_table = frequency_table.join(pd.Series(x, name="Frequency"))
frequency_table = frequency_table.join(pd.Series(r, name="Reviews"))
frequency_table = frequency_table.join(pd.Series(t, name="Average Reviews"))

# Sorting the dataframe in descending order based on # of categories
frequency_table = frequency_table.sort_values('Frequency', axis=0, ascending=False)

# Saving top-ten values in a dataframe
freq = frequency_table.iloc[:10]

# Saving the 1st output file
with open('Q2_part1.out', 'w') as f:
    for line in freq.index:
        f.write(str(freq["Country"].loc[line]) + ":" + str(freq["Frequency"].loc[line]))
        f.write('\n')
f.close()

# Plotting & saving the 3rd output file
plt.figure(figsize=(10,10))
plt.bar(x=freq["Country"][:-5], height=freq["Frequency"][:-5])
plt.title("Frequency Distribution of Top-5 Restaurants")
plt.xlabel("Category")
plt.ylabel("Count")
plt.savefig('Q2_part3.pdf')

# Sorting the dataframe in descending order based on # of reviews of categories
frequency_table = frequency_table.sort_values('Reviews', axis=0, ascending=False)

# Saving top-ten values in a dataframe
freq = frequency_table.iloc[:10]

# Saving the 2nd output file
with open('Q2_part2.out', 'w') as f:
    for line in freq.index:
        f.write(str(freq["Country"].loc[line]) + ":"
                + str(freq["Reviews"].loc[line]) + ":"
                + str(freq["Average Reviews"].loc[line]))
        f.write('\n')
f.close()