import math


def solution(m, musicinfos):
    answer = None
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

    for music in musicinfos:
        start, end, song, code = music.split(',')
        hour, minute = map(int, start.split(':'))
        start = hour * 60 + minute
        hour, minute = map(int, end.split(':'))
        end = hour * 60 + minute
        play = end - start

        code = code.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        code *= math.ceil(play / len(code))  # 실수를 올림
        code = code[:play]

        if m not in code:
            continue

        if answer == None or answer[0] < play or (answer[0] == play and answer[1] > start):
            answer = (play, start, song)

    if answer:
        return answer[-1]

    return "(None)"