from itertools import combinations_with_replacement


def solution(n, info):
    answer = [0 for _ in range(11)]
    max_num = 0
    win = False

    # 중복 조합 이용해 라이언 점수 만듦
    for res in list(combinations_with_replacement(range(0, 11), n)):
        lion_now = [0 for _ in range(11)]
        for r in res:
            lion_now[10 - r] += 1

        # 어피치와 라이언 점수 비교
        lion = 0
        peach = 0

        for i in range(11):
            if info[i] == lion_now[i] == 0:
                continue
            elif info[i] >= lion_now[i]:
                peach += (10 - i)
            elif info[i] < lion_now[i]:
                lion += (10 - i)

        # 점수 비교해 업데이트
        if lion > peach:
            win = True
            if (lion - peach) > max_num:
                max_num = lion - peach
                answer = lion_now

    if not win:
        return [-1]

    return answer