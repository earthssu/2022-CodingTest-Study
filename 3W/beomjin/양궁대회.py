
# sol1 
from itertools import combinations_with_replacement 
from collections import Counter 

def solution(n, info):
    max_diff, max_board = 0, {}
    for comb in combinations_with_replacement(range(11), n): 
        diff = 0
        cnt = Counter(comb)
        
        # compare to lion
        for i in reversed(range(11)):
            #10, 9, 8, 7, .. 
            if cnt[i] > info[10-i] and [cnt[i],info[10-i]]!=[0,0] : 
                diff += i
            elif cnt[i] <= info[10-i] and [cnt[i],info[10-i]]!=[0,0] :
                diff -= i 
        
        # diff check 
        if diff > max_diff : 
            # update diff & board
            max_diff = diff 
            max_board = cnt
        else : 
            continue
    
    if max_diff > 0 : 
        ans = [0]*11
        for key in max_board.keys():
            ans[10-key] = max_board[key]
        return ans
    else : 
        return [-1]
    
            
            
            
        
"""
    순회

    라이언은 어피치를 가장큰 점수차로 이기기 위한 n발을 각각 어떤 과녁에 맞춰야 하는지     
"""