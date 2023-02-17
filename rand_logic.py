from math import floor
from random import uniform

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