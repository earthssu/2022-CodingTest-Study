

"""
- 참고 
    https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-n%EC%A7%84%EC%88%98-%EA%B2%8C%EC%9E%84-Python
- 포인트 
    - 아무리 길어도 m*t time안에 끝나며, 그러한 정답의 문자열을 계속 길게 이어 붙인다. 
    - 그리고 p번째 순서가 되는 인덱스를 찾아서 그 부분의 값을 더해 준다. 

    - 10진수-> n진수 변환은 알고 있었는데, 
        '0123456789ABCDEF' 를 설정하는 방법은 이번에 알았다. 아래와 같다. 
        
"""
# 다른 사람 변환 코드 
def convert(num, base):
    temp = "0123456789ABCDEF" 
    q, r = divmod(num, base) #q는 다음 몫, r은 나머지 즉, n진수의 값이 된다.

    if q == 0:
        return temp[r] # 위의 temp에서 r번째 자리의 값을 가져오면, n진수 미만의 인덱스를 가질 수 밖에 없다. 
    else:
        # q를 base로 변환
        # 즉, n진수의 다음 자리를 구함
        return convert(q, base) + temp[r] # 다음자리를 더한 것을 함께해서 재귀함수로 구현해준다.



trans = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}

def n_from_10(number, n): 
    tmp = []
    while number: 
        number, mod = divmod(number, n)
        tmp.append(str(mod))
    return tmp[::-1]

def solution(n, t, m, p):
    s = ''
    ans = ''
    for i in range(m*t): 
        l = n_from_10(i,n) 
        if not l : l = ['0']
        
        for elem in l : 
            if elem in trans : s += trans[elem]
            else : s += elem 
    
    while len(ans) < t : 
        ans += s[p-1]
        p += m
        
    return ans




# 불완전한 풀이 
trans = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}

def n_from_10(number, n): 
    tmp = []
    while number: 
        number, mod = divmod(number, n)
        tmp.append(str(mod))
    return tmp[::-1]

def solution(n, t, m, p):
    num,seq = 0,0
    p -=1 
    ans = ''
    
    while True :
        if num == 0 : 
            num_li = ['0']
        else : 
            num_li = n_from_10(num,n)
            # print(f"cur num:{num}, rep:{num_li}")
            
        if seq <= p < seq+len(num_li): # 다음 시퀀스 범위 내에 있는 경우 
            # print(f"{seq} <= {p} < {seq+len(num_li)}")
            # 정답 업데이트
            i = 0 
            if seq == p : 
                if '10' <= num_li[i] <= '15': 
                    ans += trans[num_li[i]]
                else : 
                    ans += num_li[i]
                seq +=1
            else : 
                while seq!=p : 
                    seq+=1 
                    i +=1 
                else : 
                    if '10' <= num_li[i] <= '15': 
                        ans += trans[num_li[i]]
                    else : 
                        ans += num_li[i]
                seq +=1
            seq = (seq + (len(num_li)-i-1))%m
        else :  # 다음 시퀀스 범위 내에 없는 경우 이번 단어는 그냥 시퀀스 더하기만 
            seq = (seq+len(num_li))%m 
            
        print(f"seq:{seq} ans:{ans}")
        
        
        if len(ans) == t : 
            break
            
        num +=1 
        
            
    return ans 




"""
각 자연수를 n 진수로 바꾸는 코드를 구현해야 하고, 
while True : 
    n진수 값 = func(i)
    
    seq = (len(nval)+ seq )%m
    if seq == p


    if len(ans) == t: 
        break
        
    i +=1 
    

"""