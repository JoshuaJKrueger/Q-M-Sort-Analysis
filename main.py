from qSortHigh import quickSort as quickSort_H
from qSortLow import quickSort as quickSort_L
from mSort import mergeSort

from time import process_time

def main():
    x = [1,2,5,4]
    mergeSort(x)
    print(x)

if __name__ == '__main__':
    main()