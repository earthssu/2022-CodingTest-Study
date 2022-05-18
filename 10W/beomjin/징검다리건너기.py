
def solution(stones, k): 
    left =1 
    right = 2000000000
    while left <= right : 
        mid = (left+right) // 2 
        cnt = 0 
        for s in stones : 
            if s <= mid : 
                cnt +=1 
            else : 
                cnt = 0
            if cnt >= k : 
                break 
        if cnt >= k : # impossible case #징겅담리가 0보다 작아질 구간이 k보다 김
            right = mid -1 
        else : 
            left = mid + 1 
    return left
"""
- 문제 
    징검다리의 내구성이 있고, 한명이 지나갈 때 마다 그 내구성이 감소함. 
    각 인원은 k개 징검다리만큼 건너뛸 수 있음. 
    이 때 가장 많이 건널 수 있는 인원은? 
    
    binary search로 점검
    https://wiselog.tistory.com/65
"""