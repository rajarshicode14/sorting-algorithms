
def shellSort(array, n):

    interval = n // 2

    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i

            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp

        interval = interval // 2


lst = [[23, 68, 1, 9, 4, 3],
        [23, 68, 1],
        [23, 68],
        [57, 90, 12, 6, 7],
        []
    ]

for i in lst:
    shellSort(i, len(i))
    print(i)
