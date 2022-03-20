import heapq


def dijkstra(dis, path):
    heap = []
    heapq.heappush(heap, [0, 1])

    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in path[node]:
            if cost + c < dis[n]:
                dis[n] = cost + c
                heapq.heappush(heap, [cost + c, n])


def solution(N, road, K):
    INF = float('inf')
    dis = [INF] * (N+1)
    path = [[] for _ in range(N+1)]

    dis[1] = 0
    for r in road:
        path[r[0]].append([r[2], r[1]])
        path[r[1]].append([r[2], r[0]])
    dijkstra(dis, path)

    return len([x for x in dis if x <= K])