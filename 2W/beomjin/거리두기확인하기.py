dx = [-1,0,1,0]
dy = [0,1,0,-1]

def solution(places): 
    ans = []
    for place in places : 
        ans.append(is_distance(place))
    return ans 

def is_distance(place): 
    """
    input : a list of place 
        e.g. ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
    output : 1 if distance else 0 
    
    method 
        - find each item, 
        - when we find a "P", let's search around this item 
    """
    for i in range(5): 
        for j in range(5): 
            if place[i][j] == 'P': 
                # print(f"current : {i},{j}")
                for k in range(4): 
                    if 0<= i+dx[k] < 5 and 0<=j+dy[k] < 5 : 
                        if place[i+dx[k]][j+dy[k]] == 'P': 
                            # print("A neighbor is P")
                            return 0 
                        elif place[i+dx[k]][j+dy[k]] == 'O':
                            if FindP(place, i, j, dx[k], dy[k]) : 
                                # print("O around P detected")
                                return 0 
                        else : 
                            continue
    return 1
    
def FindP(place, i, j, dx_k, dy_k):
    cur_x, cur_y = i+dx_k, j+dy_k
    for k in range(4): 
        if 0<= cur_x+dx[k] < 5 and 0<=cur_y+dy[k] < 5 : 
            if [cur_x+dx[k], cur_y+dy[k]] !=[i,j] : 
                if place[cur_x+dx[k]][cur_y+dy[k]] == 'P' :
                    return 1
    return 0
        

"""
review
    1. [cur_x+dx[k], cur_y+dy[k]] !=[i,j]
    2. "out of index" technique
        if 0<= cur_x+dx[k] < 5 and 0<=cur_y+dy[k] < 5 :
    3. 주변 좌표 탐색 
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
"""
    

