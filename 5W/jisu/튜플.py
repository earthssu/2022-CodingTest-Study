def solution(s):
    answer = []
    tuple_list = []  # 문자열을 리스트로 변환해 담아놓음

    s_list = s.lstrip('{').rstrip('}').split("},{")

    for item in s_list:
        tuple_list.append(item.split(','))

    # 내부 튜플의 길이 순서대로 정렬
    tuple_list.sort(key=lambda x: len(x))

    for tup in tuple_list:
        for item in tup:
            if int(item) not in answer:
                answer.append(int(item))

    return answer


"""
tuple_list = []  # 문자열을 리스트로 변환해 담아놓음

s_list = s[1:-1].split("},{")

for item in s_list:
    tt = []  # 각 튜플을 담음
    number = ""
    for i in item:
        if i == '{':
            continue
        elif i == ',' or i == '}':
            tt.append(int(number))
            number = ""
        else:
            number += i
    if len(number) > 0 : tt.append(int(number))
    tuple_list.append(tt)
"""