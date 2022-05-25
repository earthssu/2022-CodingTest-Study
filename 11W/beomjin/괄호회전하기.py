def solution(s): 
    s = list(s)
    n = len(s)
    if n ==1 : return 0 

    ans, i = 0,0   
    while i < n : 
        if i == 0 : 
            if check(s) : ans +=1 
            i +=1     
        else : 
            s.append(s.pop(0)) 
            if check(s): ans +=1 
            i +=1 
    return ans

def check(s): 
    tmp = []
    pairs = {')':'(', ']':'[', '}':'{'}
    for elem in s : 
        if elem in ('(', '[', '{') : 
            tmp.append(elem)
        if elem in ( ')', ']', '}') : 
            if not tmp : 
                return False 
            else : 
                tmp_elem = tmp.pop()
                if tmp_elem != pairs[elem] : 
                    return False         
    return True if not tmp else False

    