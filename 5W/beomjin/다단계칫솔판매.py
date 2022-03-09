from collections import defaultdict 
from math import trunc

edgefrom = defaultdict(str)
earned = defaultdict(int)

def earning(s, money): 
    global earned
    
    # stop if s is center
    if s == "-": return
    # money condition 
    if money*0.1 < 1 : 
        earned[s] += money 
        return 
    else : 
        rest = trunc(money*0.1)
        earned[s] += money-rest
        earning(edgefrom[s], rest)
        
def solution(enroll, referral, seller, amount):
    global earned, edgefrom 
    
    for enr, edge_from in zip(enroll, referral): 
        edgefrom[enr] = edge_from
        earned[enr] = 0
    
    for s, amnt in zip(seller, amount): 
        money = amnt*100
        earning(s, money)
        
    return list(earned.values())

"""
- list 자체를 string 이나 어떤 value 자체와 비교하려 했을 때,, 
    unhasshable Type : list 에러 발생 (주의)
    (이런 실수가 잦은 것을 체크해두면 디버깅 시간 단축 가능, 주의)

- dict 의 value 를 list 로 return 하고 싶으면 list 로 형변환 해줘야 함 

- DFS 
    - dict 으로 edge_from[].append(to[]) 이런식으로 저장 
    iterative 하게 돌면서 금액 계산 
    if money %10 == ~ return 
"""