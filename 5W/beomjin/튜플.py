
def solution(s):
    set_s = set()
    s = s[2:-2]
    list_s = sorted(s.split("},{"), key=lambda x:len(x))
    
    ans = []
    for elem in list_s : 
        item = list(map(int,elem.split(',')))
        for it in item : 
            if it not in ans : ans.append(it)
    return ans
    

"""
{} 을 하나씩 돌면서, 모든 원소들을 다 더해서 튜플 만들면 되는거 아닌가? -> O(n)
    정규식으로 뽑아낼 수 있으면 젤 좋아 
아니면 가장 긴 {} 뽑아서 그거 기반으로 거기에 있는 원소 가져오거나  -> 가장 긴거 찾는거 O(n) 

아 증가하는 순서대로,, 따라가야 함 
각 튜플이 만들어지는 순서를 따라가야 했다

- DP로 풀수 있지 않을까 생각했는데, 
    각각의 {} 안에서 어떤 원소가 이미 저장된 원소이고 ,어떤 원소가 저장되지 않은 원소인지 하나씩 보아야 한다. 
    저장되어있는 원소와 저장되지 않은 원소를 구분할 수 있을까? 왜냐면 어차피 DP로  풀릴 수 있을텐데    
"""

# the other one's solution 
# 등장하는 숫자의 수를 count함 
# 가장 많이 count 된 수는 {}의 원소가 1개 일 때부터 등장헀다는 의미이기 때문에, 그것부터 출력해주면 됨

import re 
from collections import Counter
def solution(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))