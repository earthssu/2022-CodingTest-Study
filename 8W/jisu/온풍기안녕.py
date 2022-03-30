from copy import deepcopy
from sys import stdin
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

input = stdin.readline
R, C, K = map(int, input().split())
heater = []
target = []
for i in range(R):
    a = list(map(int, input().split()))
    for j in range(C):
        if 0 < a[j] < 5:
            heater.append([i, j, a[j]])
        elif a[j] == 5:
            target.append([i, j])

W = int(input())
wall = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(W):
    x, y, d = map(int, input().split())
    wall[x-1][y-1].append(d)


# 방문한 좌표 저장, 온풍기 바람
def func(x, y, f):
    if check[x][y] == 0:
        check[x][y] = 1
        board[x][y] += f
        q.append([x, y])


# 히터 테두리 온도 조절
def control_outside(board):
    for c in range(C):
        if board[0][c] > 0:
            board[0][c] -= 1
        if board[R-1][c] > 0:
            board[R-1][c] -= 1

    for r in range(1, R-1):
        if board[r][0] > 0:
            board[r][0] -= 1
        if board[r][C-1] > 0:
            board[r][C-1] -= 1


board = [[0] * C for _ in range(R)]
cnt = 0
while True:
    for i, j, d in heater:
        q = deque()
        check = [[0] * C for _ in range(R)]
        nx, ny = i + dx[d-1], j + dy[d-1]
        board[nx][ny] += 5

        if not 0 <= nx + dx[d-1] < R or not 0 <= ny + dy[d-1] < C:
            continue

        q.append([nx, ny])
        flag = 0
        for f in range(4, 0, -1):
            for _ in range(len(q)):
                x, y = q.popleft()

                if d == 1:
                    if y + 1 >= C:
                        flag = 1
                        break
                    if 1 not in wall[x][y]:
                        nx, ny = x, y + 1
                        func(nx, ny, f)
                    if x - 1 >= 0:
                        if 0 not in wall[x][y] and 1 not in wall[x - 1][y]:
                            nx, ny = x - 1, y + 1
                            func(nx, ny, f)
                    if x + 1 < R:
                        if not wall[x + 1][y]:
                            nx, ny = x + 1, y + 1
                            func(nx, ny, f)

                elif d == 2:
                    if y - 1 < 0:
                        flag = 1
                        break
                    if 1 not in wall[x][y - 1]:
                        nx, ny = x, y - 1
                        func(nx, ny, f)
                    if x - 1 >= 0:
                        if 1 not in wall[x - 1][y - 1] and 0 not in wall[x][y]:
                            nx, ny = x - 1, y - 1
                            func(nx, ny, f)
                    if x + 1 < R:
                        if 1 not in wall[x + 1][y - 1] and 0 not in wall[x + 1][y]:
                            nx, ny = x + 1, y - 1
                            func(nx, ny, f)

                elif d == 3:
                    if x - 1 < 0:
                        flag = 1
                        break
                    if 0 not in wall[x][y]:
                        nx, ny = x - 1, y
                        func(nx, ny, f)
                    if y - 1 >= 0:
                        if not wall[x][y - 1]:
                            nx, ny = x - 1, y - 1
                            func(nx, ny, f)
                    if y + 1 < C:
                        if 0 not in wall[x][y + 1] and 1 not in wall[x][y]:
                            nx, ny = x - 1, y + 1
                            func(nx, ny, f)

                else:
                    if x + 1 >= R:
                        flag = 1
                        break
                    if 0 not in wall[x + 1][y]:
                        nx, ny = x + 1, y
                        func(nx, ny, f)
                    if y - 1 >= 0:
                        if 0 not in wall[x + 1][y - 1] and 1 not in wall[x][y - 1]:
                            nx, ny = x + 1, y - 1
                            func(nx, ny, f)
                    if y + 1 < C:
                        if 1 not in wall[x][y] and 0 not in wall[x + 1][y + 1]:
                            nx, ny = x + 1, y + 1
                            func(nx, ny, f)

            if flag == 1 or len(q) == 0:
                break

    temp_b = deepcopy(board)
    for x in range(R):
        for y in range(C):
            dir = []
            if x < R - 1 and 0 not in wall[x + 1][y]:
                dir.append(4)
            if 1 not in wall[x][y]:
                dir.append(1)

            for d in dir:
                nx, ny = x + dx[d-1], y + dy[d-1]
                if 0 <= nx < R and 0 <= ny < C:
                    if board[x][y] > board[nx][ny]:
                        diff = (board[x][y] - board[nx][ny]) // 4
                        temp_b[x][y] -= diff
                        temp_b[nx][ny] += diff
                    elif board[x][y] < board[nx][ny]:
                        diff = (board[nx][ny] - board[x][y]) // 4
                        temp_b[x][y] += diff
                        temp_b[nx][ny] -= diff
    board = temp_b
    control_outside(board)

    cnt += 1
    if cnt > 100:
        break

    flag = 0
    for x, y in target:
        if board[x][y] < K:
            flag = 1
            break
    if flag == 0:
        break


print(cnt)