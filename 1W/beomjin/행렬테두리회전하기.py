def solution(rows, cols, queries): 
    arr = [[i*cols+j+1 for j in range(cols)] for i in range(rows)]
    ans = []
    local_min = None
    for qr in queries : 
        r1, c1, r2, c2 = qr[0]-1, qr[1]-1, qr[2]-1, qr[3]-1 
        tmp = arr[r1][c2]
        local_min = tmp
        # →
        for c in range(c2, c1, -1): 
            arr[r1][c] = arr[r1][c-1]
            local_min = min(local_min, arr[r1][c-1])
        # ↑
        for r in range(r1, r2): 
            arr[r][c1] = arr[r+1][c1]
            local_min = min(local_min, arr[r+1][c1])
        # ←
        for c in range(c1, c2): 
            arr[r2][c] = arr[r2][c+1]
            local_min = min(local_min, arr[r2][c+1])
        # ↓
        for r in range(r2, r1, -1): 
            arr[r][c2] = arr[r-1][c2]
            local_min = min(local_min, arr[r-1][c2])
        
        arr[r1+1][c2] = tmp
                    
        ans.append(local_min)
    return ans


"""
아 변경되는 순서를 잘못 생각했음 
- 화살표가 어떤 순서로 바뀌어야 값이 겹쳐지지 않고 업데이트 되는지 고려해야 함 
- 각각 업데이트 되는 행과 열 안에서도 어떤 순서로 바꿔야 겹치지 않고 업데이트 되는지 고려해야 함. 

- 이렇게 값을 옮기는 문제는 inverse range iteration 이 유용하다! 
    e.g.
    for i in range(큰값, 작은값, -1): 
        i 는 큰값 부터 작은값-1 까지 
"""