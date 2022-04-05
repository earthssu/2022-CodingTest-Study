def solution(m, musicinfos):
    ans = []
    for i, music in enumerate(musicinfos) : 
        st, end, title, melodies = music.split(",")
        st_h, st_m = list(map(int,st.split(":")))
        end_h, end_m = list(map(int,end.split(":")))
        st = st_h*60 + st_m 
        end = end_h*60 + end_m 
        running_time = end-st 
        
        # C#, D#, F#, G#, A#
        melodies = melodies.replace("C#","Z").replace("D#","Y").replace("F#","X").replace("G#","W").replace("A#",'V')
        m = m.replace("C#","Z").replace("D#","Y").replace("F#","X").replace("G#","W").replace("A#",'V')
        
        n, mod = divmod(running_time, len(melodies))
        played = n*melodies + melodies[:mod]
        
        if m in played : 
            ans.append((title,running_time,i))
    
    if not ans : 
        return "(None)"
    elif len(ans) == 1 : 
        return ans[0][0]
    else : 
        tmp = []
        max_run = max(list(zip(*ans[:]))[1])
        for a in ans : 
            if a[1] == max_run : 
                tmp.append(a)
            
        tmp.sort(key = lambda x: x[2])
        return tmp[0][0]
        
        
        
        


"""
- 방법 
    music info 의 item들을 돌면서 m이 subword 가 되는지를 검사해야 함 
    for music in musicinfos 
        if m in 시간에 해당하는 문자열 배열 : 
            okay 
    만약 이런게 여러개라면, 
        재생 시간이 제일 긴 음악제목 반환 
        재생 시간도 같다면 먼저 입력된 음악 반환 
    조건 일치 없다면 None 반환 
    
- 주의 
    - 반복을 돌 때 ABC 는 ABC# 안에 있는 게 아님 
    - # 이 들어간 부분인 문자열 길이를 2를 차지함, 그러나 음 하나당 1분이므로 이 부분을 
      1개의 문자열로 "미리" 변환 후, 재생된 멜로디를 구성, m 과 비교해야 함 
    - 소문자로 변환해줬으면 더 직관적이었을 뻔했다 i.e. C# -> c
    
45m
"""