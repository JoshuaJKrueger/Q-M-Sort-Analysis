from qSortHigh import quickSort as quickSort_H
from qSortLow import quickSort as quickSort_L
from mSort import mergeSort

from math import floor
from time import perf_counter as timer
from random import uniform

DEBUG = True
LIST_LEN_RANGE = (5, 6) #Range of exponents to consider (2^exp) #LOW MUST BE GREATER THAN OR EQUAL TO 10
RNG_RANGE = (0, 1000) #Domain of RNG
RNG_CUSTOM_DOMAIN = [1, 2, 3] #Options for constrained lists

def genNum(low:int=RNG_RANGE[0], upp:int=RNG_RANGE[1]) ->int:
    '''Generate a random number within [low, upp]'''
    return uniform(low,upp)

def genList(count: int, low:int=RNG_RANGE[0], upp:int=RNG_RANGE[1]) ->list:
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

def runTest(f, lst:list, isMerge:bool=False, tag:str=None) -> float:
    '''Record and return the time it takes to complete the sorting algorithm function'''
    
    t1 = timer() #Time and perform the algorithm
    if isMerge:
        f(lst)
    else:
        f(lst, 0, len(lst) - 1)
    res = timer() - t1

    if DEBUG: #Output results
        tag_text = f"[{tag}]" if tag else ''
        print(f'{tag_text} t= {res}')

    return res #Return timer result (seconds)

def main():
    #Calculate list lengths
    list_lengths = []
    for i in range(LIST_LEN_RANGE[0], LIST_LEN_RANGE[1]+1):
        list_lengths.append(2**i)
    
    #Generate lists and constrained lists
    lists = []
    for lst_len in list_lengths:
        lists.append(genList(lst_len))
    
    constrained_lists = []
    for lst_len in list_lengths:
        constrained_lists.append(genRandListFromList(lst_len, RNG_CUSTOM_DOMAIN))
    
    #Run tests
    test_count = len(list_lengths)
    test_range = range(test_count)
    print()
    print("# Mergesort")
    for i in test_range:
        runTest(mergeSort, lists[i], isMerge=True, tag=f"_|{list_lengths[i]}")
        runTest(mergeSort, constrained_lists[i], isMerge=True, tag=f"C|{list_lengths[i]}")
    print()

    print("# Quicksort (High)")
    for i in test_range:
        runTest(quickSort_H, lists[i], tag=f"_|{list_lengths[i]}")
        runTest(quickSort_H, constrained_lists[i], tag=f"C|{list_lengths[i]}")
    print()

    print("# Quicksort (Low)")
    for i in test_range:
        runTest(quickSort_L, lists[i], tag=f"_|{list_lengths[i]}")
        runTest(quickSort_L, constrained_lists[i], tag=f"C|{list_lengths[i]}")
    print()


if __name__ == '__main__':
    main()