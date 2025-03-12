def merge_sort(collection: list) -> list:

    def merge(left: list, right: list) -> list:

        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    if len(collection) <= 1:
        return collection
    mid_index = len(collection) // 2
    return merge(merge_sort(collection[:mid_index]), merge_sort(collection[mid_index:]))


a = [1, 2, 2, 32, 1, 12, 31, 23, 12, 31, 24, 2342, 35, 5]
print(merge_sort(a))
