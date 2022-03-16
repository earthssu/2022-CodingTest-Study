def solution(msg):
    ans = []
    alpha = list("abcdefghijklmnopqrstuvwxyz".upper())
    indices ={al:idx+1 for idx, al in enumerate(alpha)}
    
    largest_size = 1 
    last_index = len(indices)
    
    while msg : 
        Found = False
        w,c = '',''
        
        # Let's find a longest substring in the indices dict
        for i in range(0, len(msg)): 
            for step in reversed(range(largest_size+1)):
                if i+step > len(msg) : continue
                if msg[i:i+step] in indices :
                    Found = True 
                    w = msg[i:i+step]
                    msg = msg[i+step:]
                    break
            if Found : 
                break 
                
        # if Found : <- no need bacaues here is always Found=True
        ans.append(indices[w])
        if msg : 
            c = msg[0]
            indices[w+c] = last_index+1 
            last_index +=1 
            largest_size +=1 
    return ans

"""
- 사전에서 현재 입력과 일치하는 가장 긴 문자열 w 를 찾고 
- 그걸 찾았을 때, 출력하고 제거. 

(- 없으면 끝)
- 그 다음에도 문자열이 남아있으면 
    그 다음 문자가 남아있다는 것 자체가 가장 긴 문자열로서 이 문자가 처리가 안됐다는 의미이니까, 
    맨 마지막 에다가 이 색인 번호를 추가 

- 그 다음 또 다시 가장 긴 문자열 찾아 
"""
        
    