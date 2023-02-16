from qSortHigh import quickSort as quickSort_H
from qSortLow import quickSort as quickSort_L
from mSort import mergeSort

from math import floor
from time import perf_counter as timer
from random import uniform

DEBUG = True

def genNum(low:int, upp:int) ->int:
    return uniform(low,upp)

def genList(count: int, low:int, upp:int) ->list:
    out = []
    for _ in range(count):
        out.append(genNum(low, upp))
    return out

def genRandFromList(l:list) ->list:
    return l[floor(uniform(0, len(l)))]

def genRandListFromList(count:int, lst:list) ->list:
    out = []
    for _ in range(count):
            out.append(genRandFromList(lst))
    return out

def runTest(f, listLen:int=10, range:tuple=(0, 10), isMerge:bool=False, useList:list=None) -> float:
    a = None
    if useList is not None:
        a = genRandListFromList(listLen, useList)
    else:
        a = genList(listLen, range[0], range[1])
    
    t1 = timer()
    if isMerge:
        f(a)
    else:
        f(a, 0, listLen - 1)
    res = timer() - t1

    if DEBUG:
        sort_title = 'Merge' if isMerge else 'Quick'
        print(f'{sort_title} sort time: {res}')

    return res
    
def main():
    runTest(mergeSort, 1000, isMerge=True)
    runTest(quickSort_H, 1000)
    runTest(quickSort_H, 1000, useList=[1, 2, 3])
    runTest(quickSort_L, 5)


if __name__ == '__main__':
    main()