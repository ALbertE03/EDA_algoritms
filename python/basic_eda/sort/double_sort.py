def double_sort(collection):

    no_of_elements = len(collection)
    for _ in range(int(((no_of_elements - 1) / 2) + 1)):
        for j in range(no_of_elements - 1):

            if collection[j + 1] < collection[j]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]

            if collection[no_of_elements - 1 - j] < collection[no_of_elements - 2 - j]:
                (
                    collection[no_of_elements - 1 - j],
                    collection[no_of_elements - 2 - j],
                ) = (
                    collection[no_of_elements - 2 - j],
                    collection[no_of_elements - 1 - j],
                )
    return collection


a = [1, 2, 2, 32, 1, 12, 31, 23, 12, 31, 24, 2342, 35, 5]
print(double_sort(a))
