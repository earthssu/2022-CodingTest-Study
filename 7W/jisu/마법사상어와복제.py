import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

smell = [[0] * 4 for _ in range(4)]  # 물고기 냄새 구역 체크
fish = [[[] for _ in range(4)] for _ in range(4)]  # 물고기, 상어 위치 표시
m, s = map(int, input().split())

# 물고기 위치 좌표에 표시
for _ in range(m):
    x, y, d = map(int, input().split())
    fish[x-1][y-1].append(d-1)

# 상어 좌표
sx, sy = map(int, input().split())
sx -= 1
sy -= 1


# 상어 이동
def move_shark(x, y, cnt, del_fish, direction, check):
    global max_del, move_dir  # 물고기 최대 삭제, 이동 방향
    if cnt == 3: # 3칸 이동하므로
        if del_fish > max_del:  # 이전보다 물고기 지운 수 더 많으면
            move_dir = deepcopy(direction)
            max_del = del_fish
        return

    for d in [2, 0, 6, 4]:
        nx, ny = x + dx[d], y + dy[d]
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            continue

        flag = 0
        if [nx, ny] in check:  # 중복 이동 방지
            flag = 1
        if flag == 0:
            del_fish += len(fish[nx][ny])
        if fish[nx][ny]:
            check.append([nx, ny])
        cnt += 1
        direction.append(d)

        move_shark(nx, ny, cnt, del_fish, direction, check)

        # 초기화
        if flag == 0:
            del_fish -= len(fish[nx][ny])
        if fish[nx][ny]:
            check.pop()
        cnt -= 1
        direction.pop()


for k in range(1, s+1):
    fish_before = deepcopy(fish)  # 경로에 방해주지 않기 위해 복사
    fish_temp = [[[] for _ in range(4)] for _ in range(4)]  # 물고기 임시 이동
    for i in range(4):
        for j in range(4):
            if fish[i][j]:
                for d in fish[i][j]:
                    flag = 0
                    for _ in range(8):  # 방향별 탐색
                        nx, ny = i + dx[d], j + dy[d]
                        if 0 <= nx < 4 and 0 <= ny < 4:
                            if not (nx == sx and ny == sy):  # 상어 없음
                                if smell[nx][ny] == 0:  # 물고기 냄새 없음
                                    fish_temp[nx][ny].append(d)
                                    flag = 1
                                    break
                        d = (d + 7) % 8
                    if flag == 0:  # 이동할 방향이 어디에도 없으면 원래 자리
                        fish_temp[i][j].append(d)
    fish = fish_temp

    max_del = -1
    move_shark(sx, sy, 0, 0, deque(), deque())

    x, y = sx, sy
    for d in move_dir:
        nx, ny = x + dx[d], y + dy[d]
        if fish[nx][ny]:  # 상어 이동 자리에 물고기 있으면 없애고 냄새 남김
            fish[nx][ny] = []
            smell[nx][ny] = k
        x, y = nx, ny
    sx, sy = x, y

    # 물고기 냄새 수 조정
    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                if k - smell[i][j] == 2:  # 현재 횟수 빼기 냄새 흔적 남긴 당시 횟수가 2이면
                    smell[i][j] = 0

    # 복제 완료
    for i in range(4):
        for j in range(4):
            if fish_before[i][j]:
                for d in fish_before[i][j]:
                    fish[i][j].append(d)

ans = 0
for i in range(4):
    for j in range(4):
        ans += len(fish[i][j])

print(ans)