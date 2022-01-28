def solution(rows, columns, queries):
    """
        1. arr 생성 
        (no need) 2. 쿼리 기반으로 인덱스 체크
        3. 회전 def lotate(arr, qry)
        4. (매 회전마다) 회전한 숫자 중 최소값 리턴 def get_min(arr, qry)
    """
    #1
    arr = [[i*columns +j+1 for j in range(columns)] for i in range(rows)]
    
    #2
    def rotate(arr, qry): 
        x1, y1, x2, y2 = qry 
        width = x2-x1 
        height = y1-y2
        # 모두 붙어 있는 경우 
        if width ==1 and height == 1 : 
            clock_wise_ar = [arr[x1-1][y1-1], arr[x2-1][y1-2], arr[x2-1][y2-1], arr[x1-1][y2-1]] 
            arr[x1-1][y1-1] = clock_wise_ar[3]
            arr[x2-1][y1-1] = clock_wise_ar[0]
            arr[x2-1][y2-1] = clock_wise_ar[1]
            arr[x1-1][y2-1] = clock_wise_ar[2]
        elif width == 1 and height != 1: # 가로만 붙어 있는 경우 
            each_edge  = [arr[x1-1][y1-1], arr[x2-1][y2-1]]
            for i in range(height): 
                arr[x2-1+(i+1)][y1-1] = arr[x2-1+(i)][y1-1]
                arr[x1-1-(i+1)][y2-1] = arr[x1-1-(i)][y2-1]
            arr[x2-1][y1-2] = each_edge[0]
            arr[x1-1][y2-2] = each_edge[1]
        elif width != 1 and height == 1: # 세로만 붙어 있는 경우 
            each_edge = [arr[x2-1][y1-2], arr[x1-1][y2-1]]
            for i in range(width): 
                arr[x1-1][y1-1+(i+1)] = arr[x1-1][y1-1+(i)]
                arr[x2-1][y2-1-(i+1)] = arr[x2-1][y2-1-(i)]
        return arr
    
    def get_min(arr, qry): 
        x1, y1, x2, y2 = qry 
        a=min(arr[x1-1:x2-1][y1-1])
        b=min(arr[x2-1][y1-1:y2-1])
        c=min(arr[x1-1:x2-1][y2-1])
        d=min(arr[x1-1][y1-1:y2-1])
        return min(a,b,c,d)
    
    ans = []
    for qry in queries : 
        arr = rotate(arr, qry)
        ans.append(get_min(arr, qry))
    
    return ans
