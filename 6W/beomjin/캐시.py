def solution(cacheSize, cities):
    if not cities : return 0
    if cacheSize == 0 : 
        return len(cities)*5
    
    time = 0 #cacheSize*5 
    cities = [city.lower() for city in cities]
    cache = []
    
    for i in range(len(cities)): 
        if cities[i] in cache : 
            time += 1 
            cache.remove(cities[i])
            cache.append(cities[i])
        else : 
            time +=5
            if len(cache) == cacheSize : cache.pop(0)
            cache.append(cities[i])
    return time
"""
DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.
if a city exists in the cache, time "1", else time "5"

매번 체크해야 돼? 
    1. cities 100000개라 매번 봐도 되기는 해 : 
        Brute Force ->O(cachesize)*N
    2. 첫 설정 이후 하나씩 빼주고 더해주면 될듯 : 
        O(1)*N
    
--------------------

- 9번 테케  
    LRU 알고리즘에서 hit을 할 때, 이미 cache에 그 값이 있으면, 한 번 더 넣는 게 아니라 
    최근 자리로 끌어오는 것 
    i.e. [1,2,3,4] hit 3 -> [1,2,4,3]  \\\  not [2,3,4,3]
- 11,19,20 번 테케
    캐쉬사이즈만큼 배열을 다 채우고 반복문을 캐시사이즈 이후부터 시작한게 잘못이었다. 
    이렇게 잘못 짰을 경우, cities 길이가 캐시사이즈보다 작은 경우에는 제대로 계산을 
    못했었다.
    
- 만약 진짜 시험이었다면,,, X0X 
    이런 테케를 잡으려면, 
    - 9번은 알고리즘을 정확히 알고 있어야 했고, 
    - 11,19,20 은 최대한 hard coding피하고, general solution으로 접근하기 
"""