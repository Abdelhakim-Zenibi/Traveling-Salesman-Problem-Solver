#
# Example usage of tsp_local on a small subset of U.S. cities, more can be
# found in the TSPLib, fri26.tsp.
#
from itertools import chain
from openpyxl import load_workbook
from base import TSP
from test import matrix
from kopt import KOpt
import pandas as pd
import numpy as np
import time
def read_data_1(path):
    df = pd.read_excel(path,sheet_name='instance_3')
    df = df.drop('Unnamed: 0', axis=1)
    matr = df.values.tolist()
    matr = np.triu(matr) + np.triu(matr,1).T
    return matr

def read_data(path):
    wb = load_workbook(path, read_only=True)
    ws = wb.active
    data = [[cell.value for cell in row] for row in ws.rows]
    data1=[]
    for i in range(1,len(data)):
        ligne=[]
        for j in range(1,len(data)):
            ligne.append(data[i][j])
        data1.append(ligne)
    instance=data1
    if ({None}.issubset(chain.from_iterable(instance))):
        for i in range(len(instance)):
            for j in range(len(instance)):
                instance[j][i]=instance[i][j]
    return instance
start_time=time.time()
path2 = 'C:/Users/hp/Desktop/hakim/tsp-maroc.xlsx'

matrice = read_data_1(path2)
names = list([i for i in range(1,len(matrice)+1)])
# Load the distances
TSP.setEdges(matrice)
# Make an instance with all nodes
lk = KOpt(range(len(matrice)))
path, cost = lk.optimise()
print("Best path has cost: {}".format(cost))
res = [names[i] for i in path]
res.append(names[0])
print([i for i in res])
print (time.time()-start_time)
