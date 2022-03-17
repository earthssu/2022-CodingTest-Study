def solution(dirs):
    answer = 0
    dir = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
    visit = []
    pos = (0, 0)

    for d in dirs:
        d_pos = (pos[0]+dir[d][0], pos[1]+dir[d][1])
        if -5 <= d_pos[0] <= 5 and -5 <= d_pos[1] <= 5:
            if [pos, d_pos] not in visit and [d_pos, pos] not in visit:
                answer += 1
                visit.append([pos, d_pos])
            pos = d_pos

    return answer