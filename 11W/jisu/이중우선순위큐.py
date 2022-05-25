import heapq


def solution(operations):
    answer = [0, 0]
    queue = []
    while operations:
        opr, num = operations.pop(0).split(" ")
        if opr == 'I':
            heapq.heappush(queue, int(num))
        else:
            if queue:
                if num == "-1":
                    heapq.heapify(queue)
                    heapq.heappop(queue)
                else:
                    queue = [-x for x in queue]
                    heapq.heapify(queue)
                    heapq.heappop(queue)
                    queue = [-x for x in queue]

    if queue:
        answer = [max(queue), min(queue)]

    return answer