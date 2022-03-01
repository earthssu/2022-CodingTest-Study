
from collections import Counter 
import math

def get_subset(str1): 
    l = []
    for i in range(0, len(str1)-1): 
        if str1[i:i+2].isalpha(): 
            l.append(str1[i:i+2].lower())
    return l

def jaccard(A, B): 
    if not A and not B : 
        return 1
    A_cnt, B_cnt = Counter(A), Counter(B)   
    minmax_counter = {}
    for k in A_cnt.keys(): 
        if k in B_cnt : 
            minmax_counter[k] = (min(A_cnt[k], B_cnt[k]), max(A_cnt[k], B_cnt[k]))
        else : 
            minmax_counter[k] = (0, A_cnt[k])
    for k in B_cnt.keys():
        if k in A_cnt: continue
        else:
            minmax_counter[k] = (0, B_cnt[k]) 
    
    intersec, uni = 0,0
    for val in minmax_counter.values():
        intersec += val[0]
        uni += val[1]

    return intersec/uni
    
def solution(str1, str2):
    A = get_subset(str1)
    B = get_subset(str2)
    return math.trunc(65536*jaccard(A,B))


###############################################################################
# the other one's solution
# 집합으로 교집합과 합집합을 구하고, 
# 자카드를 계산할 때는 그 원소에 대해 min,max 를 각각 계산해서 더해준 것이 포인트
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)



###############################################################################
# 초기 잘못푼 풀이
# from collections import Counter 
# import math

# def get_subset(str1): 
#     l = []
#     for i in range(0, len(str1)-1): 
#         if str1[i:i+2].isalpha(): 
#             l.append(str1[i:i+2].lower())
#     return l

# def jaccard(A, B): 
#     if not A and not B : 
#         return 1
#     A_cnt, B_cnt = Counter(A), Counter(B)
    
#     duplicated = set(A).intersection(set(B))
#     union = set(A).union(set(B))
#     intersec, uni = len(duplicated), len(union)
    
#     for dup in duplicated: 
#         intersec += min(A_cnt[dup], B_cnt[dup])-1
#         uni += max(A_cnt[dup], B_cnt[dup])-1

#     return intersec/uni
    
# def solution(str1, str2):
#     A = get_subset(str1)
#     B = get_subset(str2)
    
#     return math.trunc(65536*jaccard(A,B))

"""
이렇게 풀면 

str1 = ' abc'
str2 = 'abbb'
인 경우 출력 값이 16384가 나와야 합니다.

만약 21845값이 나온다면 합집합 로직의 문제 입니다.
합집합 = ['ab', 'bc', 'bb', 'bb'] (o)
합집합 = ['ab', 'bc', 'bb'] (x)

이렇게 합집합 로직에 문제가 생기게 됨
"""