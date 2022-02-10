from collections import deque


def correct_location(place):
    start_point = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start_point.append([i, j])

    for start in start_point:
        queue = deque([start])
        visited = [[0] * 5 for i in range(5)]  # 방문 처리 리스트
        distance = [[0] * 5 for i in range(5)]  # 경로 길이 리스트
        visited[start[0]][start[1]] = 1

        while queue:
            y, x = queue.popleft()

            dx = [-1, 1, 0, 0]
            dy = [0, 0, 1, -1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    if place[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    if place[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0

    return 1



def solution(places):
    answer = []
    for place in places:
        answer.append(correct_location(place))

    return answer