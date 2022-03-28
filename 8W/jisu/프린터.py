from collections import deque


def solution(priorities, location):
    answer = 1
    priorities = deque(priorities)
    locate = deque([i for i in range(len(priorities))])

    while len(priorities):
        prior = priorities.popleft()
        loc = locate.popleft()

        if len(priorities) == 0 : break
        if prior < max(priorities):
            priorities.append(prior)
            locate.append(loc)
        else:
            if loc == location:
                break
            answer += 1

    return answer


"""
max 값 찾을 수 없을 때, 즉 모든 값을 pop 하여 list 비어있을 때도 고려해야 함
배열이 비어있을 땐 바로 break 해줄 필요 있음
"""