import heapq
def solution(scoville, K):
    count = 0
    scoville.sort()
    while scoville[0]<K : 
        if len(scoville) == 1 : 
            return -1 
        else : 
            min1 = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1+(min2*2))
            count +=1 
    return count


"""
    minimum을 가져야 하는 자료구조형은 heap 으로 가지고 있으면 좋음
"""
