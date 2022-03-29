from sys import stdin


input = stdin.readline
R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

W = int(input())
wall_list = [list(map(int, input().split())) for _ in range(W)]

hitter = []
target = []

for r in range(R):
    for c in range(C):
        if 1 <= board[r][c] <= 4:
            hitter.append((r, c, board[r][c]))
        elif board[r][c] == 5:
            target.append((r, c))

choco = 0
while True:
    """
    1. 바람 불게 하고
    2. 온도 조절하고
    3. board 테두리 칸 온도 조절하고
    4. 초콜릿 먹은 후에
    5. target 모든 칸이 K 이상이면 종료
    """
    flag = True
    for t in target:
        if board[t[0]][t[1]] < K:
            flag = False

    if flag:
        print(choco)
        break

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def blow_wind():
    """
    온풍기의 바람이 나오는 방향에 있는 칸은 항상 온도가 5도 올라간다.
    어떤 칸 (x, y)에 온풍기 바람이 도착해 온도가 k (> 1)만큼 상승했다면, (x-1, y+1), (x, y+1), (x+1, y+1)의 온도도 k-1만큼 상승하게 된다.
    :return:
    """


def control_temp():
    """
    모든 인접한 칸에 대해서, 온도가 높은 칸에서 낮은 칸으로 ⌊(두 칸의 온도의 차이)/4⌋만큼 온도가 조절된다.
    온도가 높은 칸은 이 값만큼 온도가 감소하고, 낮은 칸은 온도가 상승한다. 인접한 두 칸 사이에 벽이 있는 경우에는 온도가 조절되지 않는다.
    이 과정은 모든 칸에 대해서 동시에 발생한다.
    :return:
    """


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