def solution(citations):
    answer = -1

    while True:
        answer += 1
        h_more = 0
        for c in citations:
            if c >= answer:
                h_more += 1
        if h_more < answer:
            answer -= 1
            return answer