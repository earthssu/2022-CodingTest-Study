import re 
from itertools import permutations

ops = {"+": lambda x,y:x+y, "-":lambda x,y:x-y, "*":lambda x,y:x*y}

def calc(exp_li, oper):
    tmp = []
    for idx, item in enumerate(exp_li): 
        if item == oper : 
            x = tmp.pop(-1)
            y = exp_li[idx+1]
            tmp.append(ops[oper](int(x),int(y)))
            break
        else : 
            tmp.append(item)
    tmp.extend(exp_li[idx+2:])
    return  tmp 

def solution(expression):
    opers = list(set(re.findall(r'[-|+|*]', expression)))
    maxNum = -1
    for perm in permutations(opers, len(opers)): 
        exp_li = re.findall(r'\d+|[-|+|*]', expression)
        for oper in perm: 
            while oper in exp_li : 
                exp_li = calc(exp_li, oper)
        maxNum = max(maxNum, abs(exp_li[0]))
    return maxNum   
                    


"""
- ops = {"+": lambda x,y:x+y, "-":lambda x,y:x-y, "*":lambda x,y:x*y}
    - lambda 함수를 value로 가지는 dict 만드는 거 새로웠다.. 

- 브룻포스로 풀었다. 순서를 따져야 해서 순열을 사용했음.
- calc 함수 더 깔끔하게 짤 수 있었을 거 같은데.

- eval(expression)
    매개변수로 받은 expression (=식)을 문자열로 받아서, 실행하는 함수
    eval("1+2")
    eval("abs(-8)")
    eval("len([1,2,3,4])")
    eval("round(1.5)")
    출처: https://blockdmask.tistory.com/437 
"""
            