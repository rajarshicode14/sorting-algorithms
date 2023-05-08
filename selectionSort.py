
def SelectionSort(arr):

    length = len(arr)

    for i in range(length):
        minIndex = i
        for j in range(i, length):
            if arr[j] <= arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]


lst = [[23, 68, 1, 9, 4, 3],
        [23, 68, 1],
        [23, 68],
        [57, 90, 12, 6, 7]
    ]

for i in lst:
    SelectionSort(i)
    print(i)
