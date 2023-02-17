depth = 0
ops = 0

def quickSort(lst, low, high):
    global depth
    depth+=1
    if low < high:
        piv = partition(lst, low, high)
        quickSort(lst, low, piv - 1)
        quickSort(lst, piv + 1, high)
    return depth, ops

def partition(lst, low, high):
    global ops
    piv = lst[high]
    i = low - 1

    for j in range(low, high):
        ops+=1
        if lst[j] <= piv:
            i += 1
            lst[i],lst[j] = lst[j],lst[i]

    lst[i + 1],lst[high] = lst[high],lst[i + 1]

    return i + 1

# def bestBasicOps(n):
#     return ((log(n,2)-1)*n)+1

# def worstBasicOps(n):
#     return .5*n*(n-1)