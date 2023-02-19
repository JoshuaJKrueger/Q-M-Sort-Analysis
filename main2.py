from qSortHigh import quickSort as quickSort_H
from qSortLow import quickSort as quickSort_L
from mSort import mergeSort
from rand_logic import *
import main

import sys

sys.setrecursionlimit(10000)

#element_options = [i for i in range(600)]
export_key_title = "Qsort_L-md"

for i in range(10, 21):
    for j in range(10):
        element_options = [k for k in range(0, 2**(i-1))]
        #main.runTest(mergeSort, genList(2**i, 0, 1000), isMerge=True, tag=f"_|{i}", export=True, exportKey=f"{export_key_title}_{i}_{j}")
        #main.runTest(mergeSort, genRandListFromList(2**i, element_options), isMerge=True, tag=f"_|{i}", export=True, exportKey=f"{export_key_title}_{i}_{j}")

        #main.runTest(quickSort_H, genList(2**i, 0, 1000), tag=f"_|{i}", export=True, exportKey=f"{export_key_title}_{i}_{j}")
        main.runTest(quickSort_H, genRandListFromList(2**i, element_options), tag=f"_|{i}", export=True, exportKey=f"{export_key_title}_{i}_{j}")

        #main.runTest(quickSort_L, genList(2**i, 0, 1000), tag=f"_|{i}", export=True, exportKey=f"{export_key_title}_{i}_{j}")
        #main.runTest(quickSort_L, genRandListFromList(2**i, element_options), tag=f"_|{i}", export=True, exportKey=f"{export_key_title}_{i}_{j}")

print(main.results)
#Export results
main.export_csv()