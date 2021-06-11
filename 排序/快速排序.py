from typing import List


def quickSortHelper(a: List[int], i: int, j: int):
    key = a[i]
    while i < j:
        while i < j and a[j] >= key:
            j -= 1
        if i < j:
            a[i] = a[j]
        while i < j and a[i] <= key:
            i += 1
        if i < j:
            a[j] = a[i]
    a[i] = key
    return i


def quickSort(a: List[int], low: int, high: int):
    if low < high:
        standard = quickSortHelper(a, low, high)
        quickSort(a, low, standard - 1)
        quickSort(a, standard + 1, high)

a = [9,8,7,6,5,4,3,2,1]
quickSort(a, 0, len(a) - 1)
print(a)