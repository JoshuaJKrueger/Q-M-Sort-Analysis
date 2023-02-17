from qSortHigh import quickSort as quickSort_H
from qSortLow import quickSort as quickSort_L
from mSort import mergeSort
from rand_logic import *

from time import perf_counter as timer
import sys
import csv

DEBUG = True
LOG_OUTPUT = False
TEST_ITERATIONS = 10 #Sample size
LIST_LEN_RANGE = (10, 11) #Range of exponents to consider (2^exp) #LOW MUST BE GREATER THAN OR EQUAL TO 10
RNG_RANGE = (0, 1000) #Domain of RNG
RNG_CUSTOM_DOMAIN = [1, 2, 3] #Options for constrained lists

sys.setrecursionlimit(10000)

results = {}

def runTest(f, lst:list, isMerge:bool=False, tag:str=None, export:bool=True, exportKey:str=None) -> float:
    '''Record and return the time it takes to complete the sorting algorithm function'''
    
    t1 = timer() #Time and perform the algorithm
    if isMerge:
        depth, ops = f(lst)
    else:
        depth, ops = f(lst, 0, len(lst) - 1)
    res = timer() - t1

    if DEBUG: #Output results
        tag_text = f"[{tag}]" if tag else ''
        print(f'{tag_text} t= {res}')
    
    #Store results
    if not export: return
    exportKey = exportKey if exportKey else tag if tag else list.__hash__
    results[exportKey] = {
        "time": res, 
        "depth": depth,
        "ops": ops,
    }

def main():
    #Calculate list lengths
    list_lengths = []
    for i in range(LIST_LEN_RANGE[0], LIST_LEN_RANGE[1]+1):
        list_lengths.append(1<<i)
    
    #Generate lists and constrained lists
    lists = []
    for lst_len in list_lengths:
        lists.append(genList(lst_len, RNG_RANGE[0], RNG_RANGE[1]))
    
    constrained_lists = []
    for lst_len in list_lengths:
        constrained_lists.append(genRandListFromList(lst_len, RNG_CUSTOM_DOMAIN))
    
    #Run tests
    test_count = len(list_lengths)
    test_range = range(test_count)
    iter_range = range(TEST_ITERATIONS)

    for i in test_range:
        lst = lists[i]
        lst_c = constrained_lists[i]
        lst_len = list_lengths[i]
        exp = i+LIST_LEN_RANGE[0]
        if DEBUG: print("# MergeSort")
        for j in range(TEST_ITERATIONS):
            runTest(mergeSort, lst, isMerge=True, tag=f"_|{lst_len}", export=True, exportKey=f"Mergesort_{exp}_{j}")
            runTest(mergeSort, lst_c, isMerge=True, tag=f"C|{lst_len}", export=True, exportKey=f"Mergesort_C_{exp}_{j}")
        if DEBUG: print("# Quicksort (High)")
        for j in range(TEST_ITERATIONS):
            runTest(quickSort_H, lst, tag=f"_|{lst_len}", export=True, exportKey=f"Quicksort-H_{i}_{exp}_{j}")
            runTest(quickSort_H, lst_c, tag=f"C|{lst_len}", export=True, exportKey=f"Quicksort-H_C_{i}_{exp}_{j}")
        if DEBUG: print("# Quicksort (Low)")
        for j in range(TEST_ITERATIONS):
            runTest(quickSort_L, lst, tag=f"_|{lst_len}", export=True, exportKey=f"Quicksort-L_{i}_{exp}_{j}")
            runTest(quickSort_L, lst_c, tag=f"C|{lst_len}", export=True, exportKey=f"Quicksort-L_C_{i}_{exp}_{j}")


if __name__ == '__main__':
    main()

    if DEBUG and LOG_OUTPUT: #Output results
        for k, v in results.items():
            print(f"{k}: {v}")
    
    #Reformat results
    out_results = []
    for k, v in results.items():
        v["tag"] = k
        out_results.append(v)
    
    #Export results
    column_headers = ["tag", "time", "depth", "ops"]
    with open("results.csv", "w", newline='') as f:
        w = csv.DictWriter(f, column_headers)
        w.writeheader()
        w.writerows(out_results)