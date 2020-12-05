lo = 147981
hi = 691423


def check(n: int):
    if len(str(n)) != 6:
        return 0

    repeated_digit = False
    for i in range(len(str(n)) - 1):
        if str(n)[i] == str(n)[i + 1]:
            repeated_digit = True
    if not repeated_digit:
        return 0

    non_decr = True
    for i in range(len(str(n)) - 1):
        if str(n)[i] > str(n)[i + 1]:
            non_decr = False
    if not non_decr:
        return 0

    return 1


print(sum([check(i) for i in range(lo, hi + 1, 1)]))
