def balance(p):
    u, v = [], []
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i+1]
            v = p[i+1:] if i+1 < len(p) else ""
            break

    return u, v


def is_correct(p):
    stack = []
    for c in p:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] == '(':
                stack.pop(0)

    return len(stack) == 0


def solution(p):
    answer = ''

    if is_correct(p):
        return p
    else:
        if len(p) == 0:
            return ""

        u, v = balance(p)
        if is_correct(u):
            answer = u + solution(v)
        else:
            tmp = '('
            tmp += solution(v)
            tmp += ')'
            u = u[1:-1]
            for i in u:
                if i == '(':
                    tmp += ')'
                else:
                    tmp += '('

            answer += tmp

        return answer
