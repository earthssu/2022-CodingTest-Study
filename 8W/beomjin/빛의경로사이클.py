# https://techblog-history-younghunjo1.tistory.com/483

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
# 하, 좌, 상, 우


def oper(i,j,k,grid): 
    global visited 

    x,y,d = i,j,k
    cnt = 0 
    visited[x][y][d] = True
    
    while True : 
        x = (x+dx[d])%n 
        y = (y+dy[d])%m
        cnt +=1 

        if grid[x][y] == 'L': 
            d = (d-1)%4
        elif grid[x][y] == 'R': 
            d = (d+1)%4
            
        if visited[x][y][d]: 
            if (x,y,d) == (i,j,k): 
                return cnt 
            else : 
                return 0 
        visited[x][y][d] = True

def solution(grid): 
    global visited, n, m 
    n = len(grid)
    m = len(grid[0])
    ans = []

    visited = [[[False]*4 for j in range(m)] for i in range(n)]

    for i in range(n): 
        for j in range(m): 
            for k in range(4): 
                if not visited[i][j][k]: 
                    ret = oper(i, j, k, grid)
                    if ret != 0 : 
                        ans.append(ret)
    return sorted(ans)
    



"""
- 만약 좌표값이 초과되면 다음 배열로 넘어가는 것 : 
    x = (x+dx[d])%n 
- 왼쪽으로 회전해야 하거나, 오른쪽으로 회전해야 할 때 
    # 하, 좌, 상, 우
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    
    # 왼쪽 회전 
    d = (d-1)%4

    # 오른쪽 회전
    d = (d+1)%4

    # 그래 이동에도 사실은
"""







# def move_s(dx, dy): 
#     return dx, dy 

# def move_l(dx, dy): 
#     if (dx,dy) == (0,1): #-> 
#         return (-1,0) 
#     elif (dx,dy) == (0, -1): #<- 
#         return (1,0)
#     elif (dx, dy) == (1,0): #down 
#         return (0,1)
#     elif (dx, dy) == (-1,0): 
#         return (0,-1)

# def move_r(dx, dy): 
#     if (dx, dy) == (0,1): #-> 
#         return (1,0)
#     elif (dx, dy) == (0,-1): # <-
#         return(-1,0)
#     elif (dx, dy) == (1,0): #down 
#         return (0,-1)
#     elif (dx, dy) == (-1,0): #up
#         return (0,1)
    
# def solution(grid):
#     r_len = len(grid)
#     c_len = len(grid[0])
    
#     grid = [[ grid[g][i]+str(g)+str(i) for i in range(len(grid[g])) ] for g in range(len(grid))]
#     print(grid)
#     dirs = [(0,1),(0,-1),(1,0),(-1,0)]
#     ans = []
    
#     for di in dirs : 
#         cycle = [(0,0)]
#         dx, dy = di[0], di[1]
#         r,c = 0,0
        
#         while True : 
#             if grid[r][c].startswith('S'): 
#                 dx, dy = move_s(dx, dy) 
#             elif grid[r][c].startswith('L'):
#                 dx, dy = move_l(dx, dy)
#             elif grid[r][c].startswith('R'):
#                 dx, dy = move_l(dx, dy)
                
#             r = (r+dx)%r_len 
#             c = (c+dy)%c_len 
#             cycle.append((r,c))

#             if grid[r][c] == cycle[0] and (dx,dy) == (di[0], di[1]): 
#                 print("one cycle DONE")
#                 break

#         if cycle in ans : 
#             print("duplicated!")
#             continue 
#         else : 
#             print("appended cycle ->", cycle)
#             ans.append(cycle)

#     for a in ans : print(a)
#     return sorted(list(map(len, ans)))
        



# 좌표를 저장하면 안돼, 그 플로우를 저장해야 돼 

# """
# 서로 다른 사이클 알파벳만 다른게 아니라 방향도 달라야 해 
# 아니 시작하는 방향이 같아도 같은 순환이면 같은 루트를 따라 
# 어떻게 순환을 체크하지 

# 빛이 이동하는 순환경로가 경로 사이클임 
# 각 경로 사이클의 길이를 오름차순으로 정렬 

# 어느 방향에서 쏘고 어느 방향으로 나가는지가 중요할 거 같은데? 

# 기존 방향을 기준으로 다음 방향을 그대로 유지하거나 꺾거나 

# """


# 아 각 좌표에서! 어떤 방향으로 움직이는 것이 동일하면

# 각 좌표에서 서로 다른 4방향으로 움직여 보고, 방문한 적이 없어서 이동이 가능하고, 이렇게 해서 다시 돌아오면, break 이고 
# 그게 count +1 임 