from datetime import datetime


def solution(fees, records):
    answer = []
    time_dic = {}
    parking_dic = {}

    for record in records:
        time, car, park = record.split(' ')
        if car not in time_dic.keys():
            time_dic[car] = [time]
        else:
            in_time = datetime.strptime(time_dic[car][0], "%H:%M")
            out_time = datetime.strptime(time, "%H:%M")
            total = out_time - in_time

            H, M, S = str(total).split(":")

            if car not in parking_dic:
                parking_dic[car] = (int(H) * 60) + int(M)
            else:
                parking_dic[car] += (int(H) * 60) + int(M)

            del time_dic[car]

    if len(time_dic):
        for car in time_dic.keys():
            total = datetime.strptime("23:59", "%H:%M") - datetime.strptime(time_dic[car][0], "%H:%M")

            H, M, S = str(total).split(":")

            if car not in parking_dic:
                parking_dic[car] = (int(H) * 60) + int(M)
            else:
                parking_dic[car] += (int(H) * 60) + int(M)

    print(parking_dic)

    # 차량 번호 작은 순서대로 정답에 담음
    for car in parking_dic.keys():
        if parking_dic[car] <= fees[0]:
            parking_dic[car] = fees[1]
        else:
            add = parking_dic[car] - fees[0]
            if add % fees[2] > 0:
                add += (fees[2] - (add % fees[2]))

            add = (add // fees[2]) * fees[3]
            parking_dic[car] = fees[1] + add

    for key, value in sorted(parking_dic.items()):
        answer.append(value)

    return answer