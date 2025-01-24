def bubble_sort(array):
    length = len(array)
    for i in reversed(range(length)):
        swapped = False
        for j in range(i):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            break
    return array


a = [12, 31, 23, 12, 31, 24, 12, 2, 123, 1, 23, 12, 31, 23, 12, 3]

print(bubble_sort(a))
