# 온풍기 안녕! 

"""
1. 바람이 한 번 나옴 
    각 온풍기로부터 5,4,3,2,1 식으로 바람 나옴 
    벽에 막혀 있는 부분은 바람이 안나옴 

2. 온도 조절 
    주변의 값들에 대해 floor(온도차/4) 만큼 주변에 나눠줌 
    벽 있으면 조절 X 

3. 온도 1 이상인 바깥칸 온도 -1 

4. 초콜릿 +1 

5. 조사하는 칸의 온도가 K 이상인지 검사 

초콜릿 개수가 100을 넘어가면 101 출력 

- 방법 
while 반복문을 돌면서 
    
    바람 업데이트 
    (온풍기가 여러개 일 수 있음)
        온풍기 1개에 대한 업데이트 반복 
    
    온도 조절 

    온도 1 이상인 바깥칸 온도 -1 

    초콜릿 +1 

    조사칸 온도 조사 
        break or not 


- 포인트 
    - 온풍기가 벽을 고려해서 바람을 잘 업데이트 할 수 있어야 한다. 
      BFS인가? 
    - 인접 좌표를 기반으로 한 업데이트를 수행할 수 있어야 한다. 
"""

# 7 8 1
# 0 0 0 0 0 0 0 0
# 0 0 0 0 4 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 5 5 0 0 0 0
# 0 0 0 0 0 5 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 3 0 0 0
# 3
# 4 4 1
# 5 4 0
# 5 6 0

# 1

row, col, k = list(map(int, input().split()))
arr = []
walls = []
for r in row : 
    li = list(map(int, input().split()))
    arr.append(li)
num_walls = int(input())
for _ in range(num_walls): 
    r,c,t = list(map(int, input().split()))
    walls.append((r-1,c-1,t))

warm_machine = []
check_rc = []
for r in range(row): 
    for c in range(col): 
        if 0< arr[r][c]<5 : 
            warm_machine.append((r,c,arr[r][c]))
        elif arr[r][c] == 5 : 
            check_rc.append((r,c))


def bfs(r,c,di): 


def set_temperature()


chocolate = 0

while True : 

    # 바람 업데이트 
    for i in range(len(warm_machine)): 
        wr, wc, di = warm_machine[i] 
        room2 = [[0]*col for _ in range(row)]
        room2 = bfs(wr, wc, di)

        for r in range(row): 
            for c in range(col): 
                room[r][c] += room2[r][c]

    # 온도 조절 
    set_temperature()

    # 온도 1 이상인 바깥온도 -1 
    for c in range(col) : 
        if c == 0 or c == len(col)-1 : continue
        else : 
            if room[0][c] >=1 : 
                room[0][c] -=1 
            if room[-1][c] >=1 : 
                room[-1][c] -=1

    for r in range(row) : 
        if room[r][0] >= 1 : 
            room[r][0] -=1 
        if room[r][-1] >=1 : 
            room[r][0] -=1 

    # 초콜릿 
    chocolate +=1 
    if chocolate > 100 : break 

    # 온도 체크 
    done = True
    for r,c in check_rc : 
        if room[r][c] < k : 
            done = False
            break 
    if done : 
        break 


if chocolate > 100 : 
    print(101)
else : 
    print(chocolate)
