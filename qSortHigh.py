def quickSort(lst, low, high, ret):
    ret['calls']+=1

    if low < high:
        piv = partition(lst, low, high, ret)
        quickSort(lst, low, piv - 1, ret)
        quickSort(lst, piv + 1, high, ret)
    return ret

def partition(lst, low, high, ret):
    piv = lst[high]
    i = low - 1

    for j in range(low, high):
        ret['ops']+=1
        if lst[j] <= piv:
            i += 1
            lst[i],lst[j] = lst[j],lst[i]

    lst[i + 1],lst[high] = lst[high],lst[i + 1]

    return i + 1

# def bestBasicOps(n):
#     return ((log(n,2)-1)*n)+1

# def worstBasicOps(n):
#     return .5*n*(n-1)