from math import gcd, ceil, floor

def calc(w_, h_): 
    dup = 0 
    pre_x = 0
    for cor_y in range(h_): 
        cor_x = (cor_y+1)*(w_/h_) 
        dup += ceil(cor_x) - floor(pre_x)
        pre_x = cor_x
    return dup

def solution(w,h):
    gcd_number = gcd(w,h)
    w_, h_ = int(w/gcd_number), int(h/gcd_number) 
    dup = calc(w_,h_)
    
    return w*h-(dup*(int(w/w_)))
