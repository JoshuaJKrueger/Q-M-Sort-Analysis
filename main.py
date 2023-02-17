from qSortHigh import quickSort as quickSort_H
from qSortLow import quickSort as quickSort_L
from mSort import mergeSort

from math import floor
from time import perf_counter as timer
from random import uniform

DEBUG = True

def genNum(low:int, upp:int) ->int:
    '''Generate a random number within [low, upp]'''
    return uniform(low,upp)

def genList(count: int, low:int, upp:int) ->list:
    '''Generate a list of random numbers within [low, upp]'''
    out = []
    for _ in range(count):
        out.append(genNum(low, upp))
    return out

def getRandFromList(l:list) ->list:
    '''Return a random element from the provided list'''
    return l[floor(uniform(0, len(l)))]

def genRandListFromList(count:int, lst:list) ->list:
    '''Generate a list of elements randomly selected from another list'''
    out = []
    for _ in range(count):
            out.append(getRandFromList(lst))
    return out

def runTest(f, listLen:int=10, range:tuple=(0, 10), isMerge:bool=False, useList:list=None, tag:str=None) -> float:
    '''Record and return the time it takes to complete the sorting algorithm function'''

    a = None
    if useList is not None: #Generate list
        a = genRandListFromList(listLen, useList)
    else:
        a = genList(listLen, range[0], range[1])
    
    t1 = timer() #Time and perform the algorithm
    if isMerge:
        f(a)
    else:
        f(a, 0, listLen - 1)
    res = timer() - t1

    if DEBUG: #Output results
        sort_title = 'Merge' if isMerge else 'Quick'
        tag_text = f"[{tag}] " if tag else ''
        print(f'{tag_text}{sort_title} sort time: {res}')

    return res #Return timer result (seconds)

def main():
    low, upp = 10, 15

    print("# Mergesort")
    for e in range(low, upp):
        runTest(mergeSort, 2**e, isMerge=True)
    print()

    print("# Quicksort (High)")
    for e in range(low, upp):
        runTest(quickSort_H, 2**e)
    print()

    print("# Quicksort (Low)")
    for e in range(low, upp):
        runTest(quickSort_L, 2**e)


if __name__ == '__main__':
    main()