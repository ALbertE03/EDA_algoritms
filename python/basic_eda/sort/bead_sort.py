def bead_sort(sequence: list) -> list:

    if any(not isinstance(x, int) or x < 0 for x in sequence):
        raise TypeError("no puede tener elemetos negativos")
    for _ in range(len(sequence)):
        for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i + 1] += rod_upper - rod_lower
    return sequence


a = [123, 1, 23, 123, 1, 23, 12, 31, 23, 12, 31, 231, 23123, 12, 312, 34124, 12, 411, 2]
print(bead_sort(a))
