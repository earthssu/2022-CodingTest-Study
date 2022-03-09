def solution(record):
    answer = []
    nickname = {}
    for rec in record:
        rec_arr = rec.split(" ")
        if rec_arr[1] not in nickname:
            nickname[rec_arr[1]] = rec_arr[2]
        else:
            if len(rec_arr) > 2:
                nickname[rec_arr[1]] = rec_arr[2]

    for rec in record:
        rec_arr = rec.split(" ")
        if rec_arr[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(nickname[rec_arr[1]]))
        elif rec_arr[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(nickname[rec_arr[1]]))

    return answer