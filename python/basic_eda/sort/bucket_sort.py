def bucket_sort(my_list: list, bucket_count: int = 10) -> list:

    if len(my_list) == 0 or bucket_count <= 0:
        return []

    min_value, max_value = min(my_list), max(my_list)
    bucket_size = (max_value - min_value) / bucket_count
    buckets: list[list] = [[] for _ in range(bucket_count)]

    for val in my_list:
        index = min(int((val - min_value) / bucket_size), bucket_count - 1)
        buckets[index].append(val)

    return [val for bucket in buckets for val in sorted(bucket)]


a = [1, 23, 12, 3, 124, 41, 2, 34, 124, 345, 45, 47, 57, 457, 457, 4]
print(bucket_sort(a))
