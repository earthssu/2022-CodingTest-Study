def solution(n):
    answer = [0] * (n+1)
    answer[1], answer[2] = 1, 2

    for i in range(3, n+1):
        answer[i] = (answer[i-1] + answer[i-2]) % 1000000007

    return answer[n]