def solution(n, results):
    answer = 0
    wins, loses = {}, {}
    for i in range(1, n+1):
        wins[i], loses[i] = set(), set()

    for i in range(1, n+1):
        for r in results:
            if r[0] == i:
                wins[i].add(r[1])  # i가 r[1]을 이겼다
            if r[1] == i:
                loses[i].add(r[0])  # i가 r[0]한테 졌다

        for winner in loses[i]:  # i를 이긴 사람들은, i한테 진 사람들을 상대로 무조건 이긴다
            wins[winner].update(wins[i])
        for loser in wins[i]:  # i한테 진 사람들은, i를 이긴 사람들을 상대로 무조건 진다
            loses[loser].update(loses[i])

    for k in range(1, n+1):
        if len(wins[k]) + len(loses[k]) == n - 1:  # 이긴 선수와 진 선수의 합이 본인 제외와 같음
            answer += 1

    return answer