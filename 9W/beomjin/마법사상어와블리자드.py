"""
블리자드라는 마법 연습 
M 번 마법 수행 
    1. 얼음 파편 던지기 -> 구슬 파괴 
    
    2. while True 구슬 폭발
        - 폭발 구슬 조건 탐색 
        - 폭발 
        - 당기기 

    3. 구슬 변화 
        - 연속하는 구슬은 하나의 "그룹" 
        - 하나의 그룹은 두개의 구슬 A,B로 변환 
            - A : 그룹에 들어있는 구슬의 개수 
            - B : 그룹을 이루고 있는 구슬의 번호

1*(1번 구슬 폭발 개수) + 2*(2번 구슬 폭발 개수) + 3*(3번 구슬 폭발 개수)


- 방법 (나의 접근방법)
    - 구슬 파괴 okay 
    - 구슬 폭발 ★★
        - 폭발 개수 조건 : DFS로 탐색? 
            사실상 다음 이동방향이 정해져 있는 문제다.
            이동 방향 : not visit && not wall
            다음 이동방향으로 이동시키면서, DFS 
        - 폭발 : make empty 
        - 당기기 
            상어 다음 좌표부터, 하나씩 새롭게 쓰면 되지 않을까 
    - 구슬 변화 ★★
        - 그룹 조건 탐색 (DFS) 
            - 그룹 조건에 맞게 값을 또 새롭게 쓴다. 

- 포인트 (나의 접근방법)
    - 구슬 폭발, 구슬 변화 구현 
    - 두 개 함 수 모두 DFS 만 잘 구현하면 될 거 같다. 
    - 방문한 방향을 체크하고, 벽이 있는 방향을 제한 
        - 벽..을 구현하는 게 관건일 거 같다.

- 포인트 (다른 답안)
    - "구슬 폭발, 구슬 이동, 구슬 변화" 를 구현
    - ★★★
        - 배열의 크기가 한정적이고, 일정한 움직임 순서가 정해져 있으므로 그 인덱스를 1차원으로 저장한다. 
        - 모든 연산마다 그 인덱스를 순서대로 꺼내서 구슬 폭발 조건, 구슬 이동 등을 수행한다.
    - 구슬 이동 ★ 
        - 이번에 배운 구슬 이동 구현 방법
        - 구슬을 이동할 때, 
            일전에 empty value 가 있을 경우, 그 좌표를 queue에 넣고, 
            이 후 not empty value일 때, 그 빈자리에 그 값을 넣어주고, 
            not empty value자리를 queue에 넣어주는 식으로 업데이트할 수 있다. 
        - two point 를 사용하지 않고 간단한 구현방법이었다고 생각한다.
    - 구슬 그룹핑 
        - 이 부분도 마찬가지로, 인덱스를 처음부터 돌면서 
            구슬의 개수, 구슬의 종류를 구분하여, 새로운 구슬변화 리스트를 업데이트 한다. 
        - 업데이트가 끝난 이후, 기존의 좌표에 해당 값들을 순서대로 넣어준다. 

"""
# input 
# 7 1
# 0 0 0 0 0 0 0
# 3 2 1 3 2 3 0
# 2 1 2 1 2 1 0
# 2 1 1 0 2 1 1
# 3 3 2 3 2 1 2
# 3 3 3 1 3 3 2
# 2 3 2 2 3 2 3
# 2 2

##########################################
# https://kimmeh1.tistory.com/392?category=926574

import sys 
from collections import defaultdict, deque

input = sys.stdin.readline 
N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
magics = [list(map(int, input().split())) for _ in range(M)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]
count_beads = {1:0,2:0,3:0}
ordering = defaultdict(int)

def init(): 
    # shark position 
    sh_r = N//2
    sh_c = N//2 
    r,c = sh_r, sh_c
    
    # index increasing order ← ↓ → ↑
    tmp_dy = [0,1,0,-1]
    tmp_dx = [-1,0,1,0]

    # init 
    di = -1
    idx = 1
    step = 0
    ordering[idx] = [r,c]

    # 1D arr udpate 
    while idx <N*N : 
        di = (di+1)%4
        if di %2 == 0 : 
            step +=1  
        s=0 
        while s < step and idx <N*N:
            idx +=1 
            r,c = r+tmp_dy[di], c+tmp_dx[di]
            ordering[idx] = [r,c]
            s +=1 
    # print(ordering)
    
def throw_ice(d,s): 
    sh_r = N//2 
    sh_c = N//2 
    for _ in range(s): 
        sh_r = sh_r + dy[d]
        sh_c = sh_c + dx[d]
        arr[sh_r][sh_c] = 0

def move_beads(): 
    """
    - 빈칸이 있을 경우 당김
    - 좌표 자체는 orderinging 이라는 dict에서 순서대로 받아옴 
    - https://kimmeh1.tistory.com/392?category=926574
    """
    empty_pos = deque()
    
    for v in ordering.values(): 
        r,c = v
        if (r,c) == (N//2, N//2): continue  # 상어가 있는 자리 패스
        elif arr[r][c] == 0 :  # 빈칸이면 넣어야 할 자리에 넣음
            empty_pos.append((r,c))
        elif arr[r][c] >0 and empty_pos : # 이번 칸이 빈칸이 아니고, 이전에 빈칸이 있었다면 
            nr, nc = empty_pos.popleft()
            arr[nr][nc], arr[r][c] = arr[r][c], 0 
            empty_pos.append((r,c))
    
def explode_beads(): 
    visited = deque()
    count = 0 
    bead_type = -1 
    flag = False
    for v in ordering.values(): 
        r,c = v 
        if (r,c) == (N//2, N//2): continue 

        if bead_type == arr[r][c]:  # 만약 구슬 타입이 동일하면 
            visited.append((r,c)) # 방문 여부 확인
            count +=1  # 갯수 증가 
        else :  # 구슬 타입이 다르면 
            if count >=4 :  # 만약 4개 이상이면 
                flag = True  # 폭발 True
                count_beads[bead_type] += count # 폭발 구슬수 업데이트 
            while visited : # 어쨋든 다른 구슬이 나왔으니 visited는 비워줘야 한다 
                nr, nc = visited.popleft()
                if count >=4 : 
                    arr[nr][nc] = 0 # 폭발된 구슬 empty 로 
        
            # 한 턴이 종료된 경우이니 새로운 턴을 위해서 업데이트
            count = 1 
            bead_type = arr[r][c]
            visited.append((r,c))

    return flag

def make_group(): 
    """
    위의 폭발, 구슬 이동 과정이 다 끝났다면, 그룹화를 수행 
    - 각 첫 인덱스부터 조건에 맞게 새롭게 구슬을 넣을 수 있는 인덱스 리스트 구성 
    - 새로운 구슬 정보를 기존의 arr 에 업데이트 해준다 
    """
    bead_type = -1 
    count = 0 
    groups = [0]
    for v in ordering.values(): 
        r,c = v
        if (r,c) == (N//2, N//2) : continue 

        if bead_type == -1 : 
            bead_type = arr[r][c]
            count = 1 
        else : 
            if bead_type == arr[r][c]: 
                count +=1 
            else : 
                groups.append(count)
                groups.append(bead_type)
                count =1 
                bead_type = arr[r][c]

    idx = 0 
    for v in ordering.values(): 
        r,c = v 
        arr[r][c] = groups[idx]
        idx +=1 
        if idx >= len(groups): 
            break 

init()
for magic in magics : 
    d,s = magic[0]-1, magic[1]
    
    throw_ice(d,s)
    move_beads()
    while explode_beads():
        move_beads()
    make_group()

ans = 0
for k,v in count_beads.items(): 
    ans += k*v
print(ans)




