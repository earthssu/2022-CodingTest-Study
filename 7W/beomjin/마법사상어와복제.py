
"""
상어의 마법 연습 
1. 상어가 모든 물고기에게 복제 마법 시전 
    아래 5번에서 물고기 복제되어 나타남 copy 

2. 모든 물고기가 한 칸 이동 
    어떤 룰에 의해서 
    상어, 물고기냄새, 격자 범위 벗어나는 칸은 이동 X 
    물고기는 자신이 이동가능한 칸을 만날 때까지 반시계 45도 회전, 만약 불가하면 이동 X 

3. 상어 연속 3칸 이동 
    - 상어가 연속 3칸 이동할 수 없는 경우는 이동 불가한 경우 
    - 이동 중 물고기를 만나면 그 물고기들은 모두 제거, 냄새를 남김 
    - 제외되는 물고기의 수가 가장 많은 방법으로 이동, 그러한 방법이 여러가지인 경우 사전의 오름차순으로 이동
    - 이동 방법이 여러가지인 경우 사전 순 
        상1, 좌2, 하3, 우4 
        수를 이어 붙여 하나의 정수로 만듦 
        그 숫자를 오름차순으로 나열 했을 때 그게 사전 순 
        4^3 = 64가지 방법이 됨
        상어는 항상 모서리에 오기 때문에 이동 방향이 한정적임 

4. 2번 전 연습에서 생긴 냄새가 사라짐 

5. 복제 완료. 1번에서의 복제된 물고기는 1에서의 위치와 방향을 그대로 갖는다. 

물고리 위치, 방향정보, 상어 위치, 연습 횟수 S 

S번 연습 이후, 격자에 있는 물고기의 수는? 

1~8까지의 자연수 
 ←, ↖, ↑, ↗, →, ↘, ↓, ↙

"""
import copy 

m,s = list(map(int, input().split()))
arr = [[ [] for _ in range(4)]for _ in range(4)]
for _ in range(m):
    r,c,d = list(map(int, input().split()))
    arr[r-1][c-1].append(d-1)
sh_r, sh_c = tuple(map(int, input().split()))
shark = (sh_r-1, sh_c-1)

# 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 
dy = [0,-1,-1,-1,0,1,1,1]
dx = [-1,-1,0,1,1,1,0,-1]
# 상은 1, 좌는 2, 하는 3, 우는 4로
sh_dy = [-1,0,1,0]
sh_dx = [0,-1,0,1]

smell = [[0]*4 for _ in range(4)]

def fish_move(): 
    ret = [ [ [] for _ in range(4) ] for _ in range(4) ]
    for r in range(4): 
        for c in range(4): 
            while arr[r][c]: 
                d = arr[r][c].pop()
                for i in range(d, d-8, -1): 
                    i = i%8 
                    nr = r + dy[i]
                    nc = c + dx[i]
                    if 0<=nr<4 and 0<=nc<4 and (nr,nc)!=shark and not smell[nr][nc]: 
                        ret[nr][nc].append(i)
                        break
                else : 
                    ret[r][c].append(d)
    return ret 

def dfs(sh_r, sh_c, depth, cnt, visit):
    global max_cnt, eat, shark 

    # stop condition 
    if depth == 3 : 
        if cnt > max_cnt : 
            max_cnt = cnt 
            shark = (sh_r, sh_c) 
            eat = visit[:]
            # the shark coordinates will be updated when max_eat updates
        return 
    # go 
    for i in range(4): 
        sh_nr = sh_r + sh_dy[i]
        sh_nc = sh_c + sh_dx[i]
        if 0<=sh_nr<4 and 0<=sh_nc<4 : 
            if (sh_nr, sh_nc) not in visit: 
                visit.append((sh_nr, sh_nc))
                dfs(sh_nr, sh_nc, depth+1, cnt+len(arr[sh_nr][sh_nc]), visit)
                visit.pop()
            else : 
                dfs(sh_nr, sh_nc, depth+1, cnt, visit)

for _ in range(s): 
    max_cnt = -1 
    eat = []

    # 1.copy 
    # this arr would be added later 
    copied_arr = copy.deepcopy(arr)

    # 2.fish move 
    arr = fish_move()

    # 3.shark move 
    dfs(shark[0], shark[1], 0, 0, [])

    # 3.1.remove fish and smell update 
    for r,c in eat: 
        if arr[r][c] : 
            arr[r][c] = []
            smell[r][c] = 3 

    # 4.smell decreasing 
    for r in range(4): 
        for c in range(4): 
            if smell[r][c] : 
                smell[r][c] -=1 

    # 5.copy magic applied 
    for r in range(4): 
        for c in range(4): 
            arr[r][c] += copied_arr[r][c]

answer = 0
for r in range(4) : 
    for c in range(4): 
        answer += len(arr[r][c])

print(answer)


"""
- nr = r + dy[i]
    변수명 구분 확실히 하기  
    특히 DFS 처럼 재귀 쓰는 구간 ,,

- for ~ 
    if 
        braek 
  else 
  이런 경우 if문에서 break에 안걸리는 경우는 else case로 들어감 

"""


################################################################################################
# # https://ryu-e.tistory.com/107

# import copy 

# def move_fish():
#     res = [[[] for _ in range(4)] for _ in range(4)]
#     for x in range(4): 
#         for y in range(4): 
#             while temp[x][y]: 
#                 d = temp[x][y].pop()
#                 for i in range(d, d-8, -1): 
#                     i %= 8 
#                     nx, ny = x + f_dx[i], y+f_dy[i]
#                     if (nx, ny)!=shark and 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]: 
#                         res[nx][ny].append(i)
#                         break 
#                 else : 
#                     res[x][y].append(d)
#     return res 

# def dfs(x, y, dep, cnt ,visit): 
#     global max_eat, shark, eat 
#     if dep == 3 : 
#         if max_eat < cnt : 
#             max_eat = cnt 
#             shark = (x,y)
#             eat = visit[:]
#         return 
#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if 0 <= nx < 4 and 0 <= ny < 4:
#             if (nx, ny) not in visit:  # 처음 방문, cnt에 죽은 물고기 수 추가  
#                 visit.append((nx, ny))
#                 dfs(nx, ny, dep + 1, cnt + len(temp[nx][ny]), visit)
#                 visit.pop()
#             else:  # 방문한 경우
#                 dfs(nx, ny, dep + 1, cnt, visit)

# # ←, ↖,   ↑,  ↗, →, ↘, ↓, ↙
# f_dx = [0, -1, -1, -1, 0, 1, 1, 1]
# f_dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# m, s = map(int, input().split())
# fish = [list(map(int, input().split())) for _ in range(m)]
# graph = [[[] for _ in range(4)] for _ in range(4)]

# for x, y, d in fish:
#     graph[x - 1][y - 1].append(d - 1)

# shark = tuple(map(lambda x: int(x) - 1, input().split()))
# smell = [[0] * 4 for _ in range(4)]

# for _ in range(s):
#     eat = list()
#     max_eat = -1
#     # 1. 모든 물고기 복제
#     temp = copy.deepcopy(graph)
#     # 2. 물고기 이동
#     temp = move_fish()
#     # 3. 상어이동 - 백트래킹
#     dfs(shark[0], shark[1],0, 0, list())
#     for x, y in eat:
#         if temp[x][y]:
#             temp[x][y] = []
#             smell[x][y] = 3   # 3번 돌아야 없어짐
#     # 4. 냄새 사라짐 
#     for i in range(4):
#         for j in range(4):
#             if smell[i][j]:
#                 smell[i][j] -= 1
#     # 5. 복제 마법
#     for i in range(4):
#         for j in range(4):
#             graph[i][j] += temp[i][j]

# # 물고기 수 구하기 
# answer = 0
# for i in range(4):
#     for j in range(4):
#         answer += len(graph[i][j])

# print(answer)