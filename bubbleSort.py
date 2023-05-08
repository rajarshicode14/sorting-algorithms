def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


lst = [[23, 68, 1, 9, 4, 3],
       [23, 68, 1],
       [23, 68],
       [57, 90, 12, 6, 7]
       ]


for i in lst:
    bubbleSort(i)
    print(i)
