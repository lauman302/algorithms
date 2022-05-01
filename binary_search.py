def binarySearch(arr, x, left, right):
    if right <= left: # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x: # центральный элемент — искомый
        return mid
    elif x < arr[mid]: # искомый элемент меньше центрального
                       # значит следует искать в левой половине
        return binarySearch(arr, x, left, mid)
    else: # иначе следует искать в правой половине
        return binarySearch(arr, x, mid + 1, right)

# изначально мы запускаем двоичный поиск на всей длине массива
index = binarySearch(arr, x, left = 0, right = len(arr))


def binarySearchDescending(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x: # искомый элемент больше центрального
        # на этот раз все элементы больше центрального
        # располагаются в левой половине
        return binarySearchDescending(arr, x, left, mid)
    else:
        return binarySearchDescending(arr, x, mid + 1, right)
index = binarySearchDescending(arr, x, left = 0, right = len(arr))