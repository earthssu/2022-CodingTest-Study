dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def solution(grid):
    global visited, n, m
    n = len(grid)
    m = len(grid[0])

    visited = [[[0] * 4 for _ in range(m)] for _ in range(n)]
    answer = []

    for sx in range(n):
        for sy in range(m):
            for sd in range(4):
                if not visited[sx][sy][sd]:
                    res = cycle(sx, sy, sd, grid)
                    if res != 0:
                        answer.append(res)

    answer.sort()
    return answer


def cycle(sx, sy, sd, grid):
    global visited
    x, y, d = sx, sy, sd
    visited[x][y][d] = 1
    cnt = 0

    while True:
        x = (x + dx[d]) % n
        y = (y + dy[d]) % m
        cnt += 1

        if grid[x][y] == 'L':
            d = (d - 1) % 4
        elif grid[x][y] == 'R':
            d = (d + 1) % 4

        if visited[x][y][d]:
            if (x, y, d) == (sx, sy, sd):
                return cnt
            else:
                return 0

        visited[x][y][d] = 1


print(solution(["SL","LR"]))