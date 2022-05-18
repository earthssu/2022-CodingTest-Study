dy=[1,0,-1,0]
dx=[0,1,0,-1]
visited = []

from collections import deque 

def solution(m,n,picture): 
    global visited
    partion = 0 
    max_count = 0 

    def bfs(r,c, color): 
        global visited 

        que = deque()
        que.append((r,c))
        cnt = 1 

        while que : 
            r,c = que.popleft()

            for d in range(4): 
                nr = r + dy[d]
                nc = c + dx[d]
                if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited and picture[nr][nc] == color : 
                    que.append((nr,nc))
                    visited.append((nr,nc))
                    cnt +=1 
        return cnt 

    for r in range(m): 
        for c in range(n): 
            if (r,c) not in visited : 
                color = picture[r][c]
                count= bfs(r,c, color)
                partion +=1 
                if count > max_count : 
                    max_count = count 

    return [partion, max_count]
    





