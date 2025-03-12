def cocktail_shaker_sort(arr: list[int]) -> list[int]:

    start, end = 0, len(arr) - 1

    while start < end:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        end -= 1

        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        if not swapped:
            break

        start += 1

    return arr


a = [12, 31, 23, 12, 31, 24, 12, 2, 123, 1, 23, 12, 31, 23, 12, 3]

print(cocktail_shaker_sort(a))
