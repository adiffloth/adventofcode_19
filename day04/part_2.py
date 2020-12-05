lo = 147981
hi = 691423


def check(n: int):
    if len(str(n)) != 6:
        return 0

    non_decr = True
    for i in range(len(str(n)) - 1):
        if str(n)[i] > str(n)[i + 1]:
            non_decr = False
    if not non_decr:
        return 0

    rpt_cnt = 0
    rpt_cnts = [0]
    for i in range(len(str(n)) - 1):
        if str(n)[i] == str(n)[i + 1]:
            rpt_cnt += 1
        else:
            rpt_cnts.append(rpt_cnt)
            rpt_cnt = 0
    rpt_cnts.append(rpt_cnt)
    if 1 not in rpt_cnts:
        return 0

    return 1


print(sum([check(i) for i in range(lo, hi + 1, 1)]))
