from qSortHigh import quickSort as quickSort_H
from qSortLow import quickSort as quickSort_L
from mSort import mergeSort
from rand_logic import *
import main

import sys

sys.setrecursionlimit(10000)

for i in range(10):
    main.runTest(quickSort_H, genList(2**i, 0, 1000), tag=f"_|{i}", export=True, exportKey=f"qsort-h")