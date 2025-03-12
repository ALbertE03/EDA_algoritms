red = 0
white = 1
blue = 2
colors = (red, white, blue)


def dutch_national_flag_sort(sequence: list) -> list:
    if not sequence:
        return []
    if len(sequence) == 1:
        return list(sequence)
    low = 0
    high = len(sequence) - 1
    mid = 0
    while mid <= high:
        if sequence[mid] == colors[0]:
            sequence[low], sequence[mid] = sequence[mid], sequence[low]
            low += 1
            mid += 1
        elif sequence[mid] == colors[1]:
            mid += 1
        elif sequence[mid] == colors[2]:
            sequence[mid], sequence[high] = sequence[high], sequence[mid]
            high -= 1
        else:
            msg = f"The elements inside the sequence must contains only {colors} values"
            raise ValueError(msg)
    return sequence


# los elementos solo pueden ser (0,1,2)
