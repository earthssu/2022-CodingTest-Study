#https://chldkato.tistory.com/199?category=876515
# 각 행별로 접근 

import sys 
from copy import deepcopy 

input = sys.stdin.readline 

n, k = map(int, input().split())
a = list(map(int, input().split()))

fish = [[] for _ in range(n)]
for i in range(n): 
    fish[i].append(a[i])

def fish_move(n, fish): 
    fish_temp = deepcopy(fish)
    for i in range(n): 
        if fish[i]: 
            for j in range(len(fish[i])): 
                if i+1 < len(fish): 
                    if j < len(fish[i+1]): 
                        if fish[i+1][j]: 
                            if fish[i][j] > fish[i+1][j] : 
                                diff = (fish[i][j] - fish[i+1][j])//5
                                fish_temp[i][j] -=diff
                                fish_temp[i+1][j] +=diff
                        elif fish[i][j] < fish[i+1][j] : 
                            diff = (fish[i+1][j] - fish[i][j]) // 5 
                            fish_temp[i][j] += diff
                            fish_temp[i+1][j] -=diff
                if j+1 < len(fish[i]): 
                    if fish[i][j] > fish[i][j+1]: 
                        diff = (fish[i][j]-fish[i][j+1])//5
                        fish_temp[i][j] -= diff
                        fish_temp[i][j+1] += diff
                    elif fish[i][j] < fish[i][j+1]: 
                        diff = (fish[i][j+1]-fish[i][j])//5 
                        fish_temp[i][j] += diff
                        fish_temp[i][j+1] -= diff 
    return fish_temp

def make_line(): 
    blank_idx = 0 
    for i in range(n): 
        if len(fish[i]) > 1 : 
            temp = fish[i]
            fish[i] = []
            for k in temp: 
                fish[blank_idx].append(k)
                blank_idx +=1
cnt = 1 
while True : 
    # 최소 물고기 수 +1 
    min_n = sys.maxsize
    for i in range(len(fish)): 
        min_n = min(fish[i][0], min_n)
    for i in range(len(fish)): 
        if fish[i][0] == min_n : 
            fish[i][0] += 1 

    # 쌓음
    fish[1].append(fish[0][0])
    fish[0] = []

    # 쌓는 거 반복하는 부분?
    flag = 0 
    while True : 
        for i in range(len(fish)-1, 0, -1): # 거꾸로? 
            if len(fish[i]) > 1 : 
                if len(fish[i]) > len(fish)-i -1 : # 높이가 더 높이 쌓여져 있으면?? 
                    flag = 1 
                    break
                for j in range(i+1, n): 
                    if fish[j]: 
                        for v, idx in zip(fish[i], range(j, j+len(fish[i])+1)): 
                            fish[idx].append(v)
                        break 
                fish[i] = []
        if flag == 1 : 
            break

    fish = fish_move(n, fish) # 물고기 수 조절

    make_line() #  다시 1열로

    # 반쪽짜리 회전
    left, right = fish[:n//2], fish[n//2:]
    n_left = left[-1::-1]
    for l,r in zip(n_left, right): 
        r.append(l[0])

    # n//4 회전 
    left, right = right[:n//4], right[n//4:]
    for _ in range(2): 
        left = list(zip(*left[::-1]))
    for l, r in zip(left, right): 
        for ll in l : 
            r.append(ll)

    right = fish_move(n//4, right)

    fish = [[] for _ in range(n)]
    for i in range(len(right)): 
        fish[-i-1] = right[len(right)-i-1]
    make_line()

    max_n, min_n = 0, sys.maxsize
    for f in fish : 
        max_n = max(f[0], max_n)
        min_n = min(f[0], min_n)

    if max_n-min_n <=k  : 
        print(cnt)
        break       
    
    cnt +=1 


"""
정육면체 어항 

어항 정리 과정 
    1. 물고기 수가 가장 적은 어항에 물고기 +1 
        이런 어항 여러개면 모두 +1 
    2. 어항 쌓기 
        맨 왼쪽 어항을 그 옆 어항 위에 
    3. 쌓여진 어항을 공중부양 시키고 시계방향 90도 회전 눞임
        될 때까지 바복 
        공중부양 어항의 높이가 바닥의 어항의 길이보다 길면 못함 

    4. 물고기 수 조절 
        인접한 두 어항에 대해 물고기 수 차이 
        d = 차이//5 , if d > 0 : 물고기 
    5. 다시 1렬로 눞이기 
        왼쪽에 있는 어항부터 하나씩 내려서 일렬로 만들어

    6. 가운데부터 N//2 개를 공중부양, and 회전 
        2번 반복 

    7. 물고기 수 조절 
    8. 다시 1렬로 눞이기 

어항 수 N, 어항에 들어있는 물고기 수 주어짐
max(어항) - min (어항) <= K 이려면 몇번 정리해야 하는가 
N 은 4의 배수, 0<=K<=10 
"""

# N,K = map(int, input().split())
# fishes = list(map(int, input().split()))
# arr = [[]*N for _ in range(N)]



# print(N,K)
# print(fishes)

# # 1. 어항에 물고기 넣어주기 
# minfish = min(fishes)
# fishes = [f+1 for f in fishes if f==minfish else f]
# N_arranged = 0 

# while True : 
#     if N_arranged == 0 : 
#         stack(0) # 2. 어항 쌓기 (N)
#     else : 
#         stack(1)

#     rotate() # 3. 공중부양 후 눞이기
#     calc_fishes() # 4. 인접 물고기 수 조절 
#     layDown() # 5. 1열롤 정렬 

#     if stop(): # 6. return? 
#         break 
#     N_arranged +=1 

# print(N_arranged)

# def stack(): 

     
    
    
    

# 2. 어항 쌓기 (N//2)
# 3. 공주부양 후 높이기 
# 4. 인접 물고기 수 조절  
# 5. 1열로 정렬
# 6. return?  









