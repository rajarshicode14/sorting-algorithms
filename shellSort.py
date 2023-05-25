
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


arr = [23, 68, 1, 9, 4, 3, 1]
shellSort(arr, len(arr))
print('Sorted Array:')
print(arr)
