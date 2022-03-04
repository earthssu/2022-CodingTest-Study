import itertools


def solution(expression):
    answer = 0
    num_list, op_list = [], []

    num = ""
    for e in expression:
        if e == '*' or e == '+' or e == '-':
            op_list.append(e)
            num_list.append(int(num))
            num = ""
        else:
            num += e
    num_list.append(int(num))

    prior_list = list(itertools.permutations(list(set(op_list)), len(set(op_list))))

    for prior in prior_list:
        op_copy = op_list.copy()
        num_copy = num_list.copy()
        for exp in prior:
            while exp in op_copy:
                pos = op_copy.index(exp)
                num1 = num_copy.pop(pos)
                num2 = num_copy.pop(pos)
                op_copy.pop(pos)
                if exp == '+':
                    num_copy.insert(pos, num1 + num2)
                elif exp == '-':
                    num_copy.insert(pos, num1 - num2)
                else:
                    num_copy.insert(pos, num1 * num2)

        answer = max(answer, abs(num_copy[0]))

    return answer