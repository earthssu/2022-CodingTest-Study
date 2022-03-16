def rotate(arr): 
    return list(zip(*arr[::-1]))

def attach(x,y,M,key,lock_arr):
    for i in range(M): 
        for j in range(M) : 
            # y+i : N+M+M-1 인덱스까지
            lock_arr[y+i][x+j] += key[i][j] 

def detach(x,y,M,key,lock_arr): 
    for i in range(M) :
        for j in range(M) : 
            lock_arr[y+i][x+j] -=key[i][j]

def check(M,N,arr): 
    # 자물쇠 크기만큼 돌면서 확인 
    for i in range(N): 
        for j in range(N): 
            if arr[M+i][M+j] != 1 : 
                return False
    return True 

def solution(key, lock): 
    M,N = len(key), len(lock)
    rotated_key = key

    # 확장된 자물쇠
    lock_arr = [[0]*(2*M+N) for _ in range(2*M+N)]

    # 가운데 배치 
    for i in range(N) : 
        for j in range(N) : 
            lock_arr[M+i][M+j] = lock[i][j]

    # 회전하며 정답 확인 
    for y in range(N+M+1): # 0번 인덱스부터 N+M인덱스까지 
        for x in range(N+M+1): 
            for _ in range(4): 
                rotated_key = rotate(rotated_key)
                
                attach(x, y, M,rotated_key, lock_arr)
                if check(M,N,lock_arr): 
                    return True 
                detach(x, y, M,rotated_key, lock_arr)
    return False 


"""
- reference : https://velog.io/@tjdud0123/%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80-%EC%97%B4%EC%87%A0-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python

- 최대 배열이 작으니까 브룻포스로 풀어도 됐다. 

- 콘볼루션 필터 움직이는 과정이랑 매우 흡사하다.
    왜 패딩 처리할 생각을 못했을까. 
    2*키+자물쇠 만큼 패딩처리를 해서 한칸씩 움직일 수 있게 포문을 돌려준다. 
    키는 계속 90도씩 회전하면서 확인해준다.
    
- 90도 회전 시키는 코드 하나 배웠다. 
    def rotate(arr): 
        return list(zip(*arr[::-1]))
    이렇게 간결할수가

- rotate 다른 함수 
    # def rotate(key): 
    #     key_ = []
    #     for c in range(len(key)): 
    #         tmp = []
    #         for r in reversed(range(len(key[0]))):
    #             tmp.append(key[r][c]) 
    #         key_.append(tmp)
    #     return key_


"""




# Found = False
# visited = []

# def compare(key, lock): 
#     """
#     이 함수에서는 각 격자를 돌면서 lock의 좌표에 매칭되는지를 검사한다. convolution filter 움직이는 거처럼 
#     """
#     # 0,0부터 시작하며 모든 lock의 좌표 비교 
#     for lr in range(len(lock)): 
#         for lc in range(len(lock[0])): 
            
#             is_same = True 
#             for kr in range(len(key)): 
#                 for kc in range(len(key[0])): 
#                     if lock[lc+kr] != key[lc+kr]: 
#                         is_same = False
#             if not is_same : continue 
#             else : 
                
        
# def rotate(key): 
#     key_ = []
#     for c in range(len(key)): 
#         tmp = []
#         for r in reversed(range(len(key[0]))):
#             tmp.append(key[r][c]) 
#         key_.append(tmp)
#     return key_
            
# def matching(key, lock): 
#     global visited, Found
#     # visit check 
#     if key in visited : 
#         return 
#     visited.append(key)
    
#     # stopping point 
#     if compare([0,0], key, lock): 
#         Found=True
#         return
    
#     # keep going
#     matching(rotate(key), lock)

# def solution(key, lock):
#     # key = rotate(key)
#     # for i in key: print(i)
#     # return 
#     global Found, visited
#     mathcing(key, lock)
#     return Found

"""
<접근>
주어진 배열로 매칭을 해보고, 안되면 회전, 대칭이동을 통해서 가능 유무를 알아야 해. 
DFS꼴 재귀함수로 구현가능할 거 같은데 
<문제>
- 자물쇠를 벗어난 부분에 있는 '열쇠의 홈과 돌기'는 자물쇠를 여는 데 영향 X 
- '자물쇠 영역 내'에서는 
    열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확 일치
    열쇠의 돌기와 자물쇠의 돌기가 만나선 안돼
    또한 열쇠 홈의 모든 곳을 채워야 해 
"""
