def base_change(num, n):
    base = ''
    alpha = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    if num == 0:
        return '0'

    while num > 0:
        num, mod = divmod(num, n)
        if mod >= 10:
            base += alpha[mod]
        else:
            base += str(mod)

    return base[::-1]


def solution(n, t, m, p):
    answer = ''
    game_str = ''
    cnt = p

    for _ in range(t-1):
        cnt += m

    num = 0
    while len(game_str) <= cnt:
        game_str += base_change(num, n)
        num += 1

    for _ in range(t):
        answer += game_str[p-1]
        p += m

    return answer