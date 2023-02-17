from math import floor
from random import uniform

DEFAULT_LOW = 0
DEFAULT_HIGH = 100

def genNum(low:int=DEFAULT_LOW, upp:int=DEFAULT_HIGH) ->int:
    '''Generate a random number within [low, upp]'''
    return uniform(low,upp)

def genList(count: int, low:int=DEFAULT_LOW, upp:int=DEFAULT_HIGH) ->list:
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