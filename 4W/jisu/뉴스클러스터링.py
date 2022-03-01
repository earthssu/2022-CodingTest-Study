def make_set(str):
    set_list = []
    for i in range(len(str) - 1):
        tmp = str[i] + str[i+1]
        if tmp.isalpha():
            set_list.append(tmp.upper())

    return set_list


def solution(str1, str2):
    fir_set, sec_set = make_set(str1), make_set(str2)

    fir_temp, union, inter = fir_set.copy(), fir_set.copy(), []

    for s in sec_set:
        if s not in fir_temp:
            union.append(s)
        else:
            fir_temp.remove(s)

    for s in sec_set:
        if s in fir_set:
            fir_set.remove(s)
            inter.append(s)

    return int((len(inter)/len(union))*65536) if len(union) > 0 else 65536