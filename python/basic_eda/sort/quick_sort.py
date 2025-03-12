from random import randrange


def quick_sort(collection: list) -> list:

    if len(collection) < 2:
        return collection

    pivot_index = randrange(len(collection))
    pivot = collection.pop(pivot_index)

    lesser = [item for item in collection if item <= pivot]
    greater = [item for item in collection if item > pivot]

    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


a = [1, 2, 2, 32, 1, 12, 31, 23, 12, 31, 24, 2342, 35, 5]
print(quick_sort(a))
