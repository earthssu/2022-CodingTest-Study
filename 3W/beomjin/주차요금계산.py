from math import ceil 

def get_price(fees, k, v): 
    default_time, default_price, unit_time, unit_price = fees
    price = 0
    charged_time = 0
    if len(v)%2!=0 : 
        v.append([1439, "OUT"])
    for i in range(0,len(v),2): 
        in_, out_ = v[i], v[i+1]
        charged_time += out_[0] - in_[0]
    if charged_time > default_time : 
        return default_price + ceil((charged_time-default_time)/unit_time)*unit_price
    else : 
        return default_price
    
def solution(fees, records):
    """
    어쨋든 모든 차량에 대한 계산을 하는 것은 불가피해 보임 
    dict 에다가 저장하고, 그걸 저장한 것에 따라 순서대로 하나씩 꺼내서 
    계산하는 식으로. 다만 새로운 계산 값을 dict 에 넣는 식으로 
    
    해쉬 테이블, 단순 브룻포스?  
    """
    dict_records = {}
    for record in records : 
        time, carNumber, state = record.split()
        hrs, mins = map(int,time.split(":"))
        total_time = hrs*60 + mins
        if carNumber in dict_records: 
            dict_records[carNumber].append([total_time, state])
        else : 
            dict_records[carNumber] = [[total_time, state]]
    
    dict_price = {}
    for k,v in sorted(dict_records.items(), key=lambda item:item[0]):
        dict_price[k] = get_price(fees, k, v)

    return list(dict_price.values())

    # return sorted(dict_price.values(), key=dict_price.keys())