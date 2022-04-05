"""
비바라기 마법 M번 수행 
    1. 모든 구름의 이동 
    2. 구름에서 비가 내려 바구니의 물 +1 
    3. 구름 제거 
    4. 2번에서 물이 증가한 칸 (r,c)에서 물복사버그 마법 시전 
    5. 바구니에 물이 2 이상인 칸에 구름 생성, 물 -2, 3에서 사라진 칸이 아니어야 함  

바구니에 저장된 물의 총량은? 

- 방법 
    - 4번의 물복사버그 마법을 BFS로 짜야 하나? 아님 그냥 구현?
    - 그냥 구현 문제인 것 같다.
"""
# input
# 5 4
# 0 0 1 0 2
# 2 3 2 1 0
# 4 3 2 9 0
# 1 0 2 9 0
# 8 8 2 1 0
# 1 3
# 3 4
# 8 1
# 4 8

# output
# 77

import copy 

dy = [0,-1,-1,-1,0,1,1,1]
dx = [-1,-1,0,1,1,1,0,-1]

N, M = list(map(int, input().split()))
arr = []
for _ in range(N): 
    arr.append(list(map(int, input().split())))
move_info = []
for _ in range(M): 
    d_, s_ = tuple(map(int, input().split()))
    move_info.append((d_-1, s_))

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
ans = 0

def move(d,s): 
    temp = []
    for r,c in clouds : 
        for _ in range(s): 
            r = (r+dy[d])%N
            c = (c+dx[d])%N
        temp.append((r,c))
    return temp


def water_copy(): 
    # 각 4개의 좌표에 대해 대각선 검사, 물 있으면 +1 
    for r,c in pre_clouds : 
        for d in range(1,9,2): 
            nr = r + dy[d]
            nc = c + dx[d]
            if 0<=nr <N and 0 <=nc <N : 
                if arr[nr][nc] : 
                    arr[r][c] +=1 

for d,s in move_info : 

    # move clouds 
    clouds = move(d,s)

    # raining : +1 
    for c in clouds : 
        arr[c[0]][c[1]] += 1 

    # remove clouds
    pre_clouds = copy.deepcopy(clouds)
    clouds.clear()

    # water copy magic 
    water_copy()

    # next clouds 
    for r in range(N): 
        for c in range(N): 
            if (r,c) in pre_clouds : continue 
            else : 
                if arr[r][c] >=2 : 
                    clouds.append((r,c))
                    arr[r][c] -=2 


for r in range(N):
    for c in range(N): 
        ans += arr[r][c]

print(ans)



