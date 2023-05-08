def merge(arr1, arr2, arr):

    m = n = k = 0

    l1 = len(arr1)
    l2 = len(arr2)

    while n < l1 and m < l2:

        if arr1[n] <= arr2[m]:
            arr[k] = arr1[n]
            n += 1

        else:
            arr[k] = arr2[m]
            m += 1

        k += 1

    while n < l1:
        arr[k] = arr1[n]
        n += 1
        k += 1

    while m < l2:
        arr[k] = arr2[m]
        m += 1
        k += 1

    return


def mergeSort(arr):
    
    if len(arr) <= 1:
        return 
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]


    mergeSort(left)
    mergeSort(right)

    merge(left, right, arr)


lst = [[23, 68, 1, 9, 4, 3],
        [23, 68, 1],
        [23, 68],
        [57, 90, 12, 6, 7],
        []
    ]

for i in lst:
    mergeSort(i)
    print(i)