import re 

def make_bin(n): 
    tmp = ''
    while n : 
        n, mod = divmod(n, 2)
        tmp += str(mod) 
    return tmp[::-1]

def solution(n, arr1, arr2):
    ans = []
    for a1, a2 in zip(arr1, arr2): 
        N = len(arr1)
        n = a1 | a2 
        val = make_bin(n)
        val = val.replace('1','#').replace('0',' ')
        while len(val)<N : val = ' ' + val
        ans.append(val)
    return ans

"""
- 문제  
    각 두개의 arr에서 값을 하나씩 꺼내고 
        OR bit 연산을 수행, 
        이진수값을 구함. 
        그 값이 1이면 # 으로, 0이면 ' '(공백) 으로 변환 
        출력  
- 메모
    전체 지도 중 어느 하나라도 벽인 부분 => 전체에서도 벽 
    0 or 1 -> 1 
    전체 지도 중 모두 공백인 부분은 => 전체에서도 공백 
    0 or 0 -> 0 

    이진으로 바꾸고 
    이진으로 바꿈 

    연산 취해서, 1이면 # , 0 이면 ' '

"""