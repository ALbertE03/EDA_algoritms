import random


def bogo_sort(collection):

    def is_sorted(collection):
        for i in range(len(collection) - 1):
            if collection[i] > collection[i + 1]:
                return False
        return True

    while not is_sorted(collection):
        random.shuffle(collection)
    return collection


a = [1, 2, 1, 23, 12]
print(bogo_sort(a))
