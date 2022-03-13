def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    cache = ["" for _ in range(cacheSize)]  # 캐시 메모리 역할
    used = [0 for _ in range(cacheSize)]  # 참조 시간

    cities = [c.lower() for c in cities]  # 소문자로 통일
    for city in cities:
        if city in cache:  # cache hit
            idx = cache.index(city)
            used = [x+1 for x in used]
            used[idx] = 0
            answer += 1
        else:  # cache miss
            idx = used.index(max(used))
            cache[idx] = city
            used = [x + 1 for x in used]
            used[idx] = 0
            answer += 5

    return answer


# def solution_other(cacheSize, cities):
#     if cacheSize == 0:
#         return len(cities) * 5
#     answer = 0
#     cache = []
#
#     cities = [c.lower() for c in cities]  # 소문자로 통일
#     for city in cities:
#         if city in cache:
#             cache.remove(city)
#             cache.append(city)
#             answer += 1
#         else:
#             if len(cache) == cacheSize:
#                 cache.pop(0)
#             cache.append(city)
#             answer += 5
#
#     return answer