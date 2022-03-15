def solution(msg):
    answer = []
    # 알파벳 단어에 해당하는 색인번호 dic생성
    dic = {chr(i + 64): i for i in range(1, 27)}
    cnt = 27
    i = 0
    search = ''

    # i가 msg길이에 해당하는 값까지 증가되면 break
    while i < len(msg):
        # search에 한글자씩(msg[i]) 더한다.
        search += msg[i]
        # 한 글자씩 더하면서 찾으려는 단어가 이미 dic에 있다면 i인덱스 1증가, continue
        if search in dic:
            i += 1
            continue
        # 단어가 dic에 없으면 dic에 단어 추가 (색인번호는 27부터 1씩 증가해야하므로 cnt 1증가)
        else:
            dic[search] = cnt
            cnt += 1
            # 마지막 글자를 제외한 단어는 사전에 있으므로 그 단어에 해당하는 색인번호 answer에 append
            s = search[:-1]
            answer.append(dic[s])
            # search = ''로 초기화
            search = ''

    # search에 마지막 글자 남아있으니 마지막 글자의 색인번호 answer에 append
    answer.append(dic[search])
    return answer