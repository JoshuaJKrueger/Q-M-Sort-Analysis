def quickSort(lst, low, high):
    if low < high:
        piv = partition(lst, low, high)
        quickSort(lst, low, piv - 1)
        quickSort(lst, piv + 1, high)

def partition(lst, low, high):
    piv = lst[high]
    i = low - 1

    for j in range(low, high):
        if lst[j] <= piv:
            i += 1
            lst[i],lst[j] = lst[j],lst[i]

    lst[i + 1],lst[high] = lst[high],lst[i + 1]

    return i + 1

# def bestBasicOps(n):
#     return ((log(n,2)-1)*n)+1

# def worstBasicOps(n):
#     return .5*n*(n-1)