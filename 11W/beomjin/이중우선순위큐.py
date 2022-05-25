
def solution(operations):
    # que = heapq()
    que = []
    for oper in operations : 
        op, num = oper.split()
        num = int(num)
        if op == 'I': 
            que.append(num)
            que.sort()
        else : 
            if not que : continue 
            if num == 1 : 
                que.pop()
            elif num == -1 : 
                que.pop(0)
    return [0,0] if not que else [que[-1],que[0]]
            
            


"""
삽입하고, 삭제할 때, 최대 최소값을 가지고 있으면 되잖여 
"""