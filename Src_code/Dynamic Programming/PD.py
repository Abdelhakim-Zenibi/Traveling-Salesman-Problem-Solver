import random as rd
import os
import numpy as np
from functools import lru_cache
from typing import Dict, List, Tuple

import csv
import pandas as pd
import copy
from openpyxl import load_workbook
import time
from itertools import chain

start_time = time.time() 
global instance


def read_data_1(path):
    df = pd.read_excel(path,sheet_name='instance_2')
    df = df.drop('Unnamed: 0', axis=1)
    matr = df.values.tolist()
    matr = np.triu(matr) + np.triu(matr,1).T
    instance=matr
    return instance
    

def solve_tsp_dynamic_programming(first_city) -> Tuple[List, int]:
    
    # Solve TSP to optimality with dynamic programming
    
    # Get initial set {0, 1, 2, ..., tsp_size} as a frozenset because since
    # @lru_cache requires a hashable type
    N = frozenset(range(0, len(instance)))
    N = N.difference({first_city-1})
    memo: Dict[Tuple, int] = {}

    # Step 1: get minimum distance
    @lru_cache(maxsize=len(instance)**2)
    def dist(ni, N: frozenset):
        if not N:
            return instance[ni][first_city-1]

        # Store the costs in the form (nj, dist(nj, N))    
        costs = [
            (nj, instance[ni][nj] + dist(nj, N.difference({nj})))
            for nj in N
        ]
        nmin, min_cost = min(costs, key=lambda x: x[1])
        memo[(ni, N)] = nmin
        return min_cost

    best_distance = dist(first_city-1, N)

    # Step 2: get path with the minimum distance
    ni = first_city-1
    solution = [first_city]
    while N:
        ni = memo[(ni, N)]
        solution.append(ni+1)
        N = N.difference({ni})
    solution.append(first_city)
    return solution, best_distance

instance=read_data_1('C:/Users/hp/Desktop/hakim/tsp-maroc.xlsx')


first_city =1
os.system("cls")
print("\nTSP solver\n")

print("Solve with dynamic programming".center(20, '*'))
solution, dist_min=solve_tsp_dynamic_programming(first_city)
print("\n\nOPTIMAL POLICY : {}".format(solution))
print("OPTIMAL VALUE : {}".format(dist_min))
print("\n\n")
print('time :',time.time()-start_time,'s')