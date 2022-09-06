# Import libraries
import pandas as pd
import networkx as nx
import argparse

# Defining arguments for CLI
parser = argparse.ArgumentParser(description='Task #4')
parser.add_argument('addr', type=str, help='File path and name')
args = parser.parse_args()

if __name__ == '__main__':
    addr = args.addr

# Importing space-separated text file as data frame
data = pd.read_csv(addr, sep=" ", names=("a", "b"))

# Calculating # of vertices
x = list()
for i in range(len(a)):
    x.append(a[i])
    x.append(b[i])
u = pd.Series(x).unique()

# Creating network graph from edge list
G = nx.from_pandas_edgelist(data, 'a', 'b')

lines = [str(len(u), data.shape[0]),         # number of vertices and edges
         round(len(x)*100/len(u))/100,       # average number of neighbours
         nx.number_connected_components(G),  # number of components
         sum(nx.triangles(G).values()) // 3] # number of triangles

# Saving the output file
with open('Q1.out', 'w') as f:
    for line in lines:
        f.write(str(line))
        f.write('\n')
f.close()