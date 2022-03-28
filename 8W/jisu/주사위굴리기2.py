from sys import stdin
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

input = stdin.readline
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited_num = 0

dice = {
    'top': 1,  # 둘째줄 (맨 위)
    'bottom': 6,  # 넷째줄 (맨 아래)
    'up': 2,  # 첫째줄 (앞)
    'down': 5,  # 셋째줄 (뒤)
    'left': 4,
    'right': 3
}


def solution():
    x, y = 0, 0
    d = 1  # 동쪽부터 회전
    score = 0

    for _ in range(k):
        x, y, d = move_dice(x, y, d)
        d = rotate_dice(x, y, d)
        target, count = count_block(x, y)
        score += target * count

    print(score)


def count_block(sx, sy):
    global visited, visited_num
    visited_num += 1

    target = board[sx][sy]
    visited[sx][sy] = visited_num
    q = deque([(sx, sy)])
    cnt = 0

    while q:
        x, y = q.pop()
        cnt += 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if is_validate(nx, ny) and visited[nx][ny] != visited_num and board[nx][ny] == target:
                visited[nx][ny] = visited_num
                q.appendleft((nx, ny))

    return target, cnt


def move_dice(x, y, d):
    global dice
    nx = x + dx[d]
    ny = y + dy[d]

    if not is_validate(nx, ny):
        d = (d + 2) % 4
        nx = x + dx[d]
        ny = y + dy[d]

    if d == 0:  # 위로 회전
        tmp = dice['top']
        dice['top'] = dice['down']
        dice['down'] = dice['bottom']
        dice['bottom'] = dice['up']
        dice['up'] = tmp
    elif d == 1:  # 오른쪽 회전
        tmp = dice['top']
        dice['top'] = dice['left']
        dice['left'] = dice['bottom']
        dice['bottom'] = dice['right']
        dice['right'] = tmp
    elif d == 2:  # 아래로 회전
        tmp = dice['top']
        dice['top'] = dice['up']
        dice['up'] = dice['bottom']
        dice['bottom'] = dice['down']
        dice['down'] = tmp
    elif d == 3:  # 왼쪽 회전
        tmp = dice['top']
        dice['top'] = dice['right']
        dice['right'] = dice['bottom']
        dice['bottom'] = dice['left']
        dice['left'] = tmp

    return nx, ny, d


def rotate_dice(x, y, d):
    A = dice['bottom']
    B = board[x][y]
    if A > B:  # 시계방향 회전
        d = (d + 1) % 4
    elif A < B:  # 반시계방향 회전
        d = (d - 1) % 4

    return d


def is_validate(x, y):  # 범위내 좌표인지 검사
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True


solution()