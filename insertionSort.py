
def InsertionSort(arr):
    length = len(arr)
    
    for i in range(1, length):
        ref = i
        for j in range(i-1, -1, -1):
            if arr[ref] <= arr[ref - 1]:
                arr[ref], arr[ref - 1] = arr[ref - 1], arr[ref]
                ref = ref - 1
                continue
            break


lst = [[23, 68, 1, 9, 4, 3],
        [23, 68, 1],
        [23, 68],
        [57, 90, 12, 6, 7]
    ]

for i in lst:
    InsertionSort(i)
    print(i)
