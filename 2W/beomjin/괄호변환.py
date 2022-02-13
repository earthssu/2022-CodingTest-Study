
def is_right(p): 
    temp = ''
    for i, item in enumerate(p) : 
        if not temp : 
            if item == '(': temp += item 
            else : return False
        else : 
            if item == '(': temp += item
            else : 
                if temp[-1] == '(': 
                    temp = temp[:-1]
    if not temp : return True 
    else : return False 

def operate(p): 
    #1
    if not p : return ''

    #2 separate p to u and v 
    u, v = '',''
    for idx in range(2,len(p)+1,2): #### len(p)+1 을 해야 정상작동
        u, v = p[:idx], p[idx:]
        if u and u.count('(') == u.count(')'): break 
        else : continue 
    #3
    if is_right(u): 
        v = operate(v)
        return u + v
    #4
    else : 
        temp = '(' #4.1
        temp += operate(v)
        temp += ')'
        u = u[1:-1]
        for item in u : 
            if item == '(': temp += ')'
            else : temp += '('
        return temp

def solution(p):
    return operate(p)

# 48min 