"""
    작은 경우부터 brute force하게 모든 경우를 봐야 함. 
    0 1 2 3 
    01 02 03 12 13 23 
    모든 조합 

    테스트 케이스는,
        - row, col 값을 받아서 적으니까 됐다. (하드코딩 금지!)
"""
from itertools import combinations 
def is_minimal(ans, comb): 
    for a_candidate_key in ans : 
        if a_candidate_key.issubset(set(comb)): 
            return False
    return True 
    
def is_unique(relation, key):  # complexity O(n^2)
    for i in range(len(relation)): 
        item = [relation[i][idx] for idx in key]
        for j in range(i+1, len(relation)):
            if [relation[j][idx] for idx in key] == item: 
                return False
    return True 
    
def solution(relation):
    row, col = len(relation), len(relation[0])
    ans = []
    for n in range(1, col+1): 
        for comb in combinations(range(col),n): 
            if is_minimal(ans, comb) : 
                if is_unique(relation, comb): 
                    ans.append(set(comb))
    return len(ans)