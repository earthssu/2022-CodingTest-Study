def solution(priorities, location):
    li = [(p,i) for i, p in enumerate(priorities)]
    
    max_item, max_idx = max(li)
    sequence = 1
    
    while li : 
        item, idx = li.pop(0)

        if item == max_item : 
            if location == idx : 
                return sequence 
            else : 
                sequence +=1
                max_item, max_idx = max(li)
                continue 
        else : 
            li.append((item,idx))
    return sequence

"""
- J를 꺼내고 
    나머지 목록에서 J 보다 중요한게 있으면 J 를 맨 마지막에 
    else  J 출력 
    
- max heap을 쓸 수 있었더라면 더 효율적이었을 거 같은

- while 원소가 있을 떄 까지 
    하나 꺼냄, 
    나머지 중에서 맥스 값이랑 비교 
    
- 최대한 max 계산을 덜 하는게 좋다
"""



# other solution 
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer