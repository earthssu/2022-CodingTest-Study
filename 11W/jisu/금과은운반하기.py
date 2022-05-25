def solution(a, b, g, s, w, t):
    answer = int(10**16)
    left, right = 0, int(10**16)

    while left <= right:
        mid = (left + right) // 2  # 현재 시간
        gold, silver = 0, 0
        total = 0

        for i in range(len(g)):
            count = mid // (t[i] * 2)  # 물건 옮기는 횟수
            if mid % (t[i] * 2) >= t[i]:  # 편도일 경우 횟수 하나 증가
                count += 1
            city_gold = w[i] * count if w[i] * count <= g[i] else g[i]
            city_silver = w[i] * count if w[i] * count <= s[i] else s[i]
            gold += city_gold
            silver += city_silver
            total += w[i] * count if g[i] + s[i] >= w[i] * count else g[i] + s[i]

        if gold >= a and silver >= b and total >= a + b:
            right = mid - 1
            answer = min(answer, mid)
        else:
            left = mid + 1

    return answer