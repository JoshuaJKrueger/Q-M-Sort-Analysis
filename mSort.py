

def mergeSort(a):
    n = len(a)

    if (n == 1):
        return

    m = n // 2
    b = a[:m]
    c = a[m:]

    mergeSort(b)
    mergeSort(c)
    merge(a, b, c)


def merge(a, b, c):
    n = len(a)
    m = n // 2
    i = 0
    j = 0
    k = 0

    while j < m and k < n - m:
        if (b[j] <= c[k]):
            a[i] = b[j]
            j += 1
        else:
            a[i] = c[k]
            k += 1
        i += 1

    while j < m:
        a[i] = b[j]
        i += 1
        j += 1

    while k < n - m:
        a[i] = c[k]
        i += 1
        k += 1