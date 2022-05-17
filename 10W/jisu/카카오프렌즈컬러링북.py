from collections import deque


visited = [[0 for _ in range(100)] for _ in range(100)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(pixel, x, y, m, n, picture):
    cnt = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        fx, fy = queue.popleft()
        for d in range(4):
            nx, ny = fx + dx[d], fy + dy[d]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] != 1:
                if picture[nx][ny] == pixel:
                    cnt += 1
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

    return cnt


def solution(m, n, picture):
    area = [0, 0]  # 영역의 수, 최대 영역 크기

    for i in range(m):
        for j in range(n):
            if visited[i][j] != 1 and picture[i][j] != 0:
                cnt = bfs(picture[i][j], i, j, m, n, picture)
                area[0] += 1
                area[1] = max(area[1], cnt)

    return area