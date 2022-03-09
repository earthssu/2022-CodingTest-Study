def solution(record):
    """
    dict의 id를 기준으로 이름이 바뀌는 식으로 적어야 할 거 같은데 
    각 배열에다가 .. 
    들어오고 나가고는 순서대로 적어주고 
    """
    ans = []
    answer = []
    d = {}
    
    for rec in record : 
        if rec.startswith("Enter"): 
            _, user, nickname = rec.split()
            d[user] = nickname 
            ans.append([user, 1])
        elif rec.startswith("Leave") : 
            _, user = rec.split()
            ans.append([user, -1])
        elif rec.startswith("Change") : 
            _, user, nickname = rec.split()
            d[user] = nickname    
    
    # print(d)
    for an in ans : 
        if an[1] > 0 : answer.append(f"{d[an[0]]}님이 들어왔습니다.")
        else : answer.append(f"{d[an[0]]}님이 나갔습니다.")
    return answer