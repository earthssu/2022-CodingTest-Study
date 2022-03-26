from collections import defaultdict 

move = {'U':(lambda x,y: [x-1,y]), 
        'R':(lambda x,y: [x,y+1]),
        'D':(lambda x,y: [x+1,y]), 
        'L':(lambda x,y: [x,y-1]) }

def OOB(elem):
    r,c = elem
    return 0<=r<11 and 0<=c<11 ### 

def solution(dirs):
    if len(dirs) == 1 : return 1 

    N = 11 
    visited = defaultdict(list)
    count = 0
    r,c = 5,5
    for d in dirs: 
        if OOB(move[d](r,c)): 
            rn, cn = move[d](r,c)
            if (rn,cn) in visited[(r,c)] : 
                pass
            else : 
                # 서로 쌍방향으로 이동여부를 저장해야 함에 주의!
                visited[(r,c)].append((rn,cn))
                visited[(rn,cn)].append((r,c))
                count +=1 
            r,c = rn, cn
        else : 
            continue 
        # print(visited)
    return count
        
        
"""
해당하는 좌표를 시작점으로 해서 간 적이 있으면 되거든 

hash, 2dArr
"""
        
        
        