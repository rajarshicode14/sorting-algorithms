def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        flag = 0

        for j in range(n - 1):

            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                flag = 1

        if flag == 0:
            break
        

lst = [[23, 68, 1, 9, 4, 3],
        [23, 68, 1],
        [23, 68],
        [57, 90, 12, 6, 7]
        ]


for i in lst:
    bubbleSort(i)
    print(i)
