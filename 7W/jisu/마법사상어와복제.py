from itertools import permutations


bowl = [[[] for _ in range(4)] for _ in range(4)]  # 어항
direction = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5:(0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}
dic_four = {1: (-1, 0), 2: (0, -1), 3: (1, 0), 4: (0, 1)}


M, S = map(int, input().split())
fir_dic = []  # 물고기 초기 위치 저장
for m in range(M):
    r, c, dic = map(int, input().split())
    bowl[r-1][c-1].append(dic)
    fir_dic.append((r-1, c-1))

R, C = map(int, input().split())
bowl[R-1][C-1].append('F')

print(bowl)

def move_fish(bowl, r, c, dic):
    fir = dic
    while True:
        nr = r+direction[dic][0]
        nc = c+direction[dic][1]

        if 0 <= nr <= 3 and 0 <= nc <= 3 and bowl[nr][nc] != 'F' and bowl[nr][nc] != 'S':
            bowl[r][c].remove(fir)
            bowl[nr][nc].append(dic)
            break
        else:
            if dic == 1:
                dic = 8
            else:
                dic -= 1

    print(bowl)

for i in range(4):
    for j in range(4):
        if len(bowl[i][j]) > 0:
            for b in bowl[i][j]:
                if b != 'F' and b != 'S':
                    move_fish(bowl, i, j, b)

print(bowl)

# def move_shark(bowl, r, c):
#     fish_max = 0
#     dic_value = 0
#     for per in list(permutations([1, 2, 3, 4], 3)):
#         flag = True
#         fish_cnt = 0
#         for p in per:
#             nr = r + dic_four[p][0]
#             nc = c + dic_four[p][1]
#             if 0 <= nr <= 4 and 0 <= nc <= 4:
#                 r, c = nr, nc
#                 if bowl[nr][nc] > 0:
#                     bowl[nr][nc] = 0  # 물고기 제외
#                     fish_cnt += 1
#             else:
#                 flag = False
#                 break
#         if flag:
#             if fish_max < fish_cnt:
#                 fish_max = fish_cnt



"""
5 2
4 3 5
1 3 5
2 4 2
2 1 6
3 4 4
4 2
"""