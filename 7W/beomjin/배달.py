"""
- 그래프의 한점에서 다른 점들로의 최소비용이면은 다익스트라 알고리즘으로 구현하면 쉽게 풀릴 것 간다.
https://codlingual.tistory.com/200
"""
# 다익스트라 알고리즘 
import heapq 
    
def solution(N, road, K): 
    inf = 10e9 
    graph = [[]*N for _ in range(N)]
    distance = [inf]*N
    
    for r in road : 
        st, dest, cost = r 
        graph[st-1].append((dest-1, cost))
        graph[dest-1].append((st-1, cost))
        
    def dijkstra(start): 
        q = []
        distance[start] = 0 
        heapq.heappush(q, (0, start)) #cost, start point 
        
        while q : 
            # 꺼내기
            dist, st = heapq.heappop(q)
            
            # 이미 방문 또는 현재 값이 최소인지 체크 
            if distance[st] < dist : continue
            
            # 그게 아니라면, 연결된 주변 노드들로 최소값 업데이트하고 다시 넣어줌 
            for connected in graph[st]: 
                # connected_node => st지점에서의 [dest, cost] 들
                # 그니까 st에서 dest로 도달하는 cost를 담은 정보들이 들어있음 
                cost = dist + connected[1] 
                # 비교대상 cost = 현재 dist + 연결된 노드로 이동하는데에 드는 cost
                if cost < distance[connected[0]] : 
                    # 즉 dest로 이동하는 데 드는 비용이 더 싸면
                    distance[connected[0]] = cost
                    heapq.heappush(q, (cost, connected[0]))
    dijkstra(0)
    ans = 0
    for d in distance : 
        if d <=K : ans +=1 
    return ans



N=5	
road=[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]	
K=3

print(solution(N,road,K)) #answer: 4





# 이거 왜 업뎃이 제대로 안되지.
def solution(N, road, K):
    inf = 10e9
    adjacent = [[inf]*N for _ in range(N)] 
    
    # adjacent information update 
    for r in road : 
        a,b,c = r
        adjacent[a-1][b-1] = c  
        adjacent[b-1][a-1] = c 
        adjacent[a-1][a-1] = 0
        adjacent[b-1][b-1] = 0 
    
    for i in adjacent : 
        print(i)
    print()
        
    # 다익스트라? 쓰면 모든 점에서의 그걸 구할 수 있긴한데, O(n**3) 임. 
    for k in range(N): 
        for i in range(N):
            for j in range(N): 
                print(i,j,"and",k)
                if adjacent[i][j] > adjacent[i][k] + adjacent[k][j]: 
                    adjacent[i][j] = adjacent[i][k]+adjacent[k][j]
                    print(f"updated: {adjacent[i][k]}+{adjacent[k][j]}")
    for i in adjacent : 
        print(i)
    
    ans = 1 
    for i in range(1,N): 
        if adjacent[0][i] <= K : 
            print(f"1->{i+1}  dis:{adjacent[0][i]}")
            ans +=1 
    return ans 

"""
1번 -> 타마을 
N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문 가능 

가장 짧은 경로를 찾아야 하는구나 1번 마을에서 
K보다 최소 경로가 짧은 구간만 이동 가능한 것 
"""