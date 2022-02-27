from itertools import combinations


def solution(relation):
    targets = [i for i in range(len(relation[0]))]
    key_arr = []

    for c in range(1, len(relation[0])+1):
        candidate_list = list(combinations(targets, c))
        for cnd in candidate_list:
            attribute_list = []
            overlap = False
            for rel in relation:
                attr = []
                for n in list(cnd):
                    attr.append(rel[n])
                if attr not in attribute_list:
                    attribute_list.append(attr)
                else:
                    overlap = True
                    break
            if not overlap:
                for k in key_arr:
                    if set(k).issubset(set(cnd)):
                        break
                else:
                    key_arr.append(cnd)

    return len(key_arr)
