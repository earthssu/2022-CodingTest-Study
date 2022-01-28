from math import inf

def solution(s):
    if  len(s) == 1 : return 1 
    
    min_len = inf 
    min_str = ""
    for n in range(len(s)):  # unit size 
        unit_size = n+1
        tmp = ""
        st = 0
        cnt = 1
        while st <= len(s)-1 : 
            a_unit = s[st:st+unit_size]
            if a_unit == s[st+unit_size: st+2*(unit_size)]: # if same : count up, st up  
                cnt +=1
                st += unit_size
            else : # if not same : tmp up, count reset, st up 
                if cnt >=2 : 
                    tmp += str(cnt) + a_unit 
                else : 
                    tmp += a_unit
                cnt = 1
                st += unit_size
        #### ?
        # if st == len(s)-1 
        # if st > len(s)-1 
        
        if len(tmp) < min_len : 
            min_len = len(tmp)
            min_str = tmp
    
    return min_len