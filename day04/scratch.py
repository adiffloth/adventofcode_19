def fu(n):
    rpt_cnt = 0
    rpt_cnts = [0]
    for i in range(len(str(n)) - 1):
        if str(n)[i] == str(n)[i + 1]:
            rpt_cnt += 1
            rpt_cnts.append(rpt_cnt)
        else:
            rpt_cnt = 0
    if not max(rpt_cnts) == 1:
        # print(n)
        return 0
    else:
        return 1


print(fu(112233))
print(fu(123444))
print(fu(111122))
