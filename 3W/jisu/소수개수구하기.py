import math


def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False

    return True


def solution(n, k):
    answer = 0
    k_split = ""

    while n:
        k_split += str(n % k)
        n = n // k

    k_split = k_split[::-1]

    zero_split = k_split.split("0")

    for num in zero_split:
        if num != '':
            if is_prime(int(num)):
                answer += 1

    return answer
