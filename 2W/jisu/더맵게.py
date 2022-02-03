import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1

        sc_fir = heapq.heappop(scoville)
        sc_sec = heapq.heappop(scoville)
        heapq.heappush(scoville, sc_fir + (sc_sec * 2))

        answer += 1

    return answer
