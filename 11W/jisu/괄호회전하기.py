from collections import deque


def is_correct(arr):
    stack = []
    for a in arr:
        if a == '[' or a == '{' or a == '(':
            stack.append(a)
        else:
            if len(stack) == 0: return False
            else:
                temp = stack.pop()
                if (a == ']' and temp != '[') or (a == '}' and temp != '{') or (a == ')' and temp != '('):
                    return False

    return True if len(stack) == 0 else False


def solution(s):
    answer = 0
    for x in range(len(s)):
        s_rotation = deque(s)
        for i in range(x):
            pop = s_rotation.popleft()
            s_rotation.append(pop)
        flag = is_correct(s_rotation)
        if flag:
            answer += 1

    return answer


print(solution("[](){}"))