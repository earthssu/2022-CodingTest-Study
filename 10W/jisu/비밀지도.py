def binary(num1, num2, n):
    result = ""

    while num1 > 0 or num2 > 0:
        num1, mod1 = divmod(num1, 2)
        num2, mod2 = divmod(num2, 2)
        if mod1 == 1 or mod2 == 1:
            result += "1"
        elif mod1 == 0 and mod2 == 0:
            result += "0"

    zero = n - len(result) if n - len(result) > 0 else 0
    result += "0" * zero

    return result[::-1]


def solution(n, arr1, arr2):
    answer = [''] * n
    for i in range(n):
        answer[i] = binary(arr1[i], arr2[i], n)
        answer[i] = answer[i].replace("0", " ").replace("1", "#")

    return answer