dx = [1, 1, 0]
dy = [0, 1, 1]

def remove(row, col, board_list): 
    remove_pos = set()
    remove_true = None

    # calculate which subsquare can be removed
    for r in range(row):
        for c in range(col):
            if board_list[r][c] == '' : 
                continue
            remove_true = True
            for i in range(3):
                if 0<=r+dx[i]<row and 0<=c+dy[i]<col : 
                    if board_list[r][c] != board_list[r+dx[i]][c+dy[i]] :
                        remove_true = False
                        break
                else : 
                    remove_true = False
                    break
            if remove_true : 
                remove_pos.add((r,c))
                for i in range(3):
                    remove_pos.add((r+dx[i], c+dy[i]))
                
    # make empty
    for removed in remove_pos :
        board_list[removed[0]][removed[1]] = ''
        
    # pull down
    for r in reversed(range(row)):
        for c in range(col):
            d = 1
            while 0<r+d<row and board_list[r+d][c] == '': 
                board_list[r+d][c] = board_list[r+d-1][c]
                board_list[r+d-1][c] = ''
                d +=1

    return board_list, len(remove_pos)
    
def solution(row, col, board):
    board_list = [list(line) for line in board]
    removed_num = None
    ans = 0
    while removed_num!=0:
        board_list, removed_num = remove(row, col, board_list)
        ans += removed_num
    return ans

"""
set  
    - can only add a value that is immutable (like a string or a tuple) to a set.
    - immutable object (수정불가능한 객체)
"""
            

    