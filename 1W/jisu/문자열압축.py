def solution(s):
    answer = 1000000

    for unit in range(1, len(s) // 2 + 2):
        result = ''
        tmp = s[:unit]
        cnt = 1

        for i in range(unit, unit+len(s), unit):
            if tmp == s[i:i+unit]:
                cnt += 1
            else:
                if cnt == 1:
                    result += tmp
                else:
                    result = result + str(cnt) + tmp
                cnt = 1
                tmp = s[i:i+unit]

        answer = min(answer, len(result))

    return answer
