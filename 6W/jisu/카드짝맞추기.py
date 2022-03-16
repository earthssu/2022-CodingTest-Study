from collections import deque

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def end_game(board):
    if board.count('0') == 16:
        return True
    return False


def remove_element(board, num):
    board = board.replace(num, '0')
    return board


def move(b, y, x, dy, dx):
    ny, nx = y + dy, x + dx
    if 0 <= ny < 4 and 0 <= nx < 4 and b[ny * 4 + nx] == "0":  # 범위 안에 들면서 0 (아무 요소 없음)
        return move(b, ny, nx, dy, dx)
    else:
        if 0 <= ny < 4 and 0 <= nx < 4:  # 범위 안에 들면서 0 말고 다른 숫자
            return (ny, nx)
        else:  # 범위 내 아님
            return (y, x)


def solution(board, r, c):
    answer = 0
    b = ""

    # board를 배열에서 긴 문자열로 바꿔줌
    for i in range(4):
        for j in range(4):
            b += str(board[i][j])

    q = deque([])

    cnt = 0
    enter = -1  # enter을 클릭했던 위치
    q.append((r, c, b, cnt, enter))
    s = set()

    while q:
        y, x, b, c, e = q.popleft()
        pos = 4 * y + x

        if (y, x, b, e) in s:  # 한 번 방문했던 곳이면 넘어감
            continue
        s.add((y, x, b, e))

        if end_game(b):  # 게임 끝나면 이동 횟수 반환
            return c

        # 4 방향 이동 (커서 누른 방향으로 한 칸 이동)
        for (dy, dx) in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 4 and 0 <= nx < 4:
                q.append((ny, nx, b, c+1, e))

        # Ctrl + 4 방향 이동 (이동 방향에서 가장 가까운 카드로 한 번에 이동)
        for (dy, dx) in d:
            ny, nx = move(b, y, x, dy, dx)
            if ny == y and nx == x:
                continue
            # 자기 자신 아닐 경우에만 q에 넣어줌
            q.append((ny, nx, b, c+1, e))

        # enter를 하는 경우
        if b[pos] != 0:
            if e == -1:
                n_e = pos
                q.append((y, x, b, c+1, n_e))
            else:
                if e != pos and b[e] == b[pos]:  # 엔터 두 번 누르지 않고 같은 요소 맞음
                    b = remove_element(b, b[e])
                    q.append((y, x, b, c+1, -1))

    return answer