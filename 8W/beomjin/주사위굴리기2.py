"""
주사위의 이동 한 번 
    1. 이동 방향으로 굴러감 
        만약 이동 방향으로 가지 못하면 이동방향의 반대방향으로 한 칸 이동
    2. 도착한 칸 (x,y) 에 대한 점수 획득 
    3. 주사위 아랫면의 정수 VS 좌표 (x,y)위의 정수 B 를 비교해 다음 방향 결정
        - A>B : 시계 90도 회전 
        - A<B : 반시계 90도 회전 
        - A=B : 그대로 
    
이동 시에도 B 가 있을 때, 그러한 칸 C를 count 
score = B*C 

- 방법 
    주사위를 k 만큼 반복문으로 굴려가며 
        해당하는 위치에서 동서남북으로 BFS를 수행한다. 
        탐색가능할 때까지 수행하고, 해당 점수를 구해온다. 

        A,B 값을 비교해서 다음 방향을 업데이트한다. 

- 포인트 
    - 주사위 회전 구현 (흠) 
    - BFS 구현
    - 방향 회전 및 방향 전환 : 인덱스 활용 
"""
# input 
# 4 5 1
# 4 1 2 3 3
# 6 1 1 3 3
# 5 6 1 3 2
# 5 5 6 5 5
#  output
# 4

from collections import deque 

n,m,k = list(map(int,input().split()))
arr = []
for _ in range(n): 
    li = list(map(int,input().split()))
    arr.append(li)

# →, ↓, ←, ↑
dy = [0,1,0,-1]
dx = [1,0,-1,0]
r,c = 0,0
di = 0
score = 0 

dice = [2,4,1,3,5,6]


def bfs(r,c, B, visit): 
    global cnt

    queue = deque()
    queue.append((r,c))
    visit.append((r,c))
    
    while queue: 
        r,c = queue.popleft()

        for i in range(4): 
            nr_, nc_ = r+dy[i], c+dx[i]
            if 0<=nr_<n and 0<=nc_<m and (nr_, nc_) not in visit: 
                if arr[nr_][nc_] == B : 
                    cnt +=1 
                    visit.append((nr_, nc_))
                    queue.append((nr_, nc_))

for _ in range(k): 
    cnt = 1

    # 방향 업데이트 
    nr, nc = r+dy[di], c+dx[di]
    if 0<=nr<n and 0<=nc<m : # 해당 방향으로 이동 가능 
        B = arr[nr][nc]
        bfs(nr, nc, B, [])
        score += B*cnt 
        r,c = nr, nc
    else : # 반대 방향으로 이동해서 수행 
        di = (di+2)%4
        nr, nc = r+dy[di], c+dx[di]
        B = arr[nr][nc]
        bfs(nr, nc, B, [])
        score += B*cnt 
        r,c = nr, nc


    # 주사위 회전 
    # 동, 서로 이동할 때는 0,4번 인덱스 값은 고정 
    # 남, 북으로 이동할 때는 1,3번 인덱스 값은 고정 
    if di == 0 : #동쪽으로 이동 
        dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
    elif di == 1: # 남쪽으로 이동 
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
    elif di == 2 : # 서쪽으로 이동 
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
    elif di == 3 : # 북쪽으로 이동 
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0] 

    A = dice[5]

    if A>B : 
        di = (di+1)%4
    elif A<B : 
        di = (di-1)%4

print(score)
    


"""
- bfs 는 재귀함수가 아님 
    q 구성 
    while q : 
        item = q.pop()
        for i in range(4): 
            if 조건 매칭 & not visit
                q.append(주변 탐색 아이템) 
                visit.append(주변 탐색 아이템)

- 주사위를 굴리는 방법 잘 알아두기 
"""


