import math 
from math import ceil 

def _k_digits(n,k): 
    digits_as_str =  ""
    
    # find largest digit 
    i=0
    while n > pow(k,i): 
        i +=1
    largest_digit, dg = i-1, i-1
    # print(f"largest pos : {largest_digit}")

    # calculate it iteratively
    while n >= k : 
        # m=0
        for m in reversed(range(k)):
            if pow(k,dg)*m <= n : break
        digits_as_str += str(m)
        if m!=0 : n = n%(pow(k,dg)*m)
        dg -= 1
        
    if n < k : 
        digits_as_str += str(n)
    return digits_as_str

def k_digits(n,k): 
    tmp = ''
    while n > 0 : 
        n, mod = divmod(n, k)
        tmp += str(mod)
    return tmp[::-1]
    
def is_prime(x):
    """
    root(x) 만큼까지 포문 돌면서,, 
    """
    if x < 2 : return False
    else : 
        for i in range(2,int(math.sqrt(x)+1)):
            if x%i == 0 : return False
        return True 

def solution(n, k):
    """
    10진수 n을 모양만 k진수로 바꾸었을 때, 각 수에서 얻을 수 있는 소수의 개수 
    여기서 소수는 10진수 기준의 소수 
    소수들이 아래의 조건도 만족해야 함 
    """
    k_num = k_digits(n,k)
    # print(k_num)
    st, end = 0, 0 
    ans = 0
    while st < len(k_num) : 
        # print(st, end)
        while end < len(k_num) and k_num[end]!='0': 
            end +=1
        if st == end : candidate = k_num[st]
        else : candidate = k_num[st:end]
        # print(f"candidate: {candidate}")
        if candidate and is_prime(int(candidate)) :
            # print(f"can isn't prime?")
            ans +=1 
        st, end = end+1, end+1
    return ans

    """
    def k_digits 함수에 문제가 있음 
            def k_digits(n, k) :
                jinsu = ''
                while n > 0 :
                    n, mod = divmod(n, k)
                    jinsu += str(mod)
                return jinsu[::-1]
    이걸 넣어주면 잘 됨 

    배운 점 
        - k digits 함수 구현법 
            작은 것 부터 divmod 함수 적용  
            마지막에 str[::-1]
        - is_prime 함수 복습 
            range(2, int(sqrt(x))+1) 하면 더 빠름 
        - clu = jinsu(n, k).split('0')
            여기는 window 안 쓰고 0으로 split 그냥 간단히 해버림 ㅠ 
    """