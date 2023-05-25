def partition(arr, lower, upper):

    pivot = lower

    while lower < upper:
        while lower <= len(arr) - 1 and arr[pivot] >= arr[lower]:
            lower += 1

        while arr[pivot] < arr[upper]:
            upper -= 1

        if lower < upper:
            arr[lower], arr[upper] = arr[upper], arr[lower]

    arr[upper], arr[pivot] = arr[pivot], arr[upper]

    return upper

def __quickSort(arr, lower, upper):

    if lower < upper:
        loc = partition(arr, lower, upper)
        __quickSort(arr, lower, loc - 1)
        __quickSort(arr, loc + 1, upper)

def quickSort(arr):
    lower = 0
    upper = len(arr) - 1

    __quickSort(arr, lower, upper)


lst = [[23, 68, 1, 9, 4, 3],
        [23, 68, 1],
        [23, 68],
        [57, 90, 12, 6, 7],
        []
    ]

for i in lst:
    quickSort(i)
    print(i)

