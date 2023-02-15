
def quickSort(listToSort, low, high):
    if low>=high: return

    pivot = partition(listToSort, low, high)
    quickSort(listToSort, low, pivot)
    quickSort(listToSort, pivot+1, high)

def partition(a, low, high):
    p = a[low]
    p_i = low
    j = low
    i = low+1
    while i<=high:
        if a[i]<p:
            a[i],a[j] = a[j],a[i]
            if p_i==j:
                p_i=i
            j+=1
        i+=1
    if a[j]>p:
        a[j],a[p_i] = a[p_i],a[j]
    return j

#best case
#log_2 = log(n, 2)
#n*log_2 -(n-1)

#worst case
#return n*(n-1)*0.5