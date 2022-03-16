def strtotime(s): 
    hours, mins, secs = list(map(int,s.split(':')))
    return secs+(mins*60)+(hours*3600)
    
def timetostr(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + sㄴ  
    
def solution(play_time, adv_time, logs):
    if play_time == adv_time : return "00:00:00"
    
    play_time = strtotime(play_time)
    adv_time = strtotime(adv_time)
    all_time = [0 for i in range(play_time+1)]
    
    # 변동이 있는 구간만 체크 
    for l in logs : 
        st, end = l.split('-')
        st, end = strtotime(st), strtotime(end)
        all_time[st] +=1 
        all_time[end] -=1 
    
    # 각 변동구간 누적 
    for i in range(1, len(all_time)): 
        all_time[i] = all_time[i] + all_time[i-1]
    
    # 각 구간 i의 값이 0시점부터 누적 값이 되도록 계산 
    for i in range(1, len(all_time)): 
        all_time[i] = all_time[i] + all_time[i-1]
        
    # 가장 큰 누적 구간은 광고 런닝타임만큼 뺀 구간 
    most_view = 0
    max_time = 0
    for i in range(adv_time-1, play_time):
        if i >= adv_time:
            if max(most_view, all_time[i]-all_time[i-adv_time]) > most_view : 
                most_view = all_time[i]-all_time[i-adv_time]
                max_time = i-adv_time+1 
        # adv_time 이전의 most_view 업데이트
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1
    
    # print(timetostr(max_time))
    return timetostr(max_time)
    

        
"""
- 전체길이에서 특정 구간만큼의 구간합이 가장 큰 부분을 구하는 문제 
    라는 걸 처음부터 파악하지 못한 게 아쉽다 

- 이렇게 구간합 문제라는 것을 파악했고, 특정 시작과 종료 구간이 있다면 
    prefix 방법을 생각했어야 했는데, 누적합을 떠올렸어야 했는데 다 보려고 했다는 것도 아쉽다.

- 전체 시간이 100시간 즉, 초로 환산하면 360000칸의 array가 나오므로 이렇게 돌아도 그렇게 복잡도가 
    크지 않았을 것이라는 것을 빠르게 눈치채지 못해서 아쉽다.

- reference: https://dev-note-97.tistory.com/156
"""

        
"""
전체길이에서 특정 구간만큼의 구간합이 가장 큰 부분을 구하는 문제 

시작점은 매번 각 로그 시점이고.. 그 시작점에 몇 개의 로그가 동시에 존재하는지를 봐야함 

전체 영상시간인 O(N)으로 해결이 가능해 
각 로그를 돌면서 그걸 만들어 줄 수 있고, 각 시작 시점마다,, 

구간합 문제였으니까 저번의 그 파괴되지않은건물 문제를 딱 떠올렸어야 했는데 

"""





########### Time Error
# from collections import defaultdict 

# def strtotime(s): 
#     hours, mins, secs = list(map(int,s.split(':')))
#     return secs+(mins*60)+(hours*3600)
    
# def solution(play_time, adv_time, logs):
    
#     if play_time == adv_time : 
#         return "00:00:00"
    
#     partial_sum = defaultdict(int)
#     adv_running = strtotime(adv_time)
    
#     for log in logs : 
#         log_start, log_end = log.split("-")
#         partial_sum[log_start] = 0
        
#     for key in partial_sum.keys(): 
#         adv_start = strtotime(key)
#         for log in logs : 
#             log_st, log_end = log.split("-")
#             log_st, log_end = strtotime(log_st), strtotime(log_end)
#             for log_i in range(log_st, log_end): 
#                 if adv_start <= log_i < adv_start+adv_running: 
#                     partial_sum[key] +=1
                    
#     ans = []
#     for k, v in partial_sum.items(): 
#         max_val = max(partial_sum.values())
#         if partial_sum[k] == max_val: 
#             ans.append(k)
            
#     return sorted(ans)[0]