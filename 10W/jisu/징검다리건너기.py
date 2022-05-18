def solution(stones, k):
    left, right = 1, max(stones)
    answer = 1

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        flag = True
        for s in stones:
            if s < mid:
                cnt += 1
                if cnt == k:
                    flag = False
                    break
            else:
                cnt = 0

        if flag:
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1

    return answer