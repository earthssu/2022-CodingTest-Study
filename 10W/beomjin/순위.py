"""
- method 
    1. Floyde Washal Alogirithm 
        to update relationship between ij which is from ik and kj 
        e.g if ik==1 and kj==1 : ij=1 
    2. set winner_dict and loser_dict to 
        and then update them via a rule 
            for example, if an winner wins againt i, and then losers from i have to be beaten by the winner 

- Programmers/Lv3/Floyde-Washal★/
"""

def solution(n, results): 
    graph = [[0]*(n+1) for _ in range(n+1)]

    for win, lose in results : 
        graph[win][lose] = 1 
        graph[lose][win] = -1 

    for k in range(1,n+1): 
        for i in range(1,n+1): 
            for j in range(1,n+1): 
                if i ==j : continue 
                if graph[i][j] in [-1,1]: continue 
                if graph[i][k]==1 and graph[k][j] == 1 : 
                    graph[i][j] = 1 
                    graph[j][i] = graph[j][k] = graph[k][i] = -1 
    ans = 0
    for r in graph : 
        if r.count(0) == 2 : 
            ans +=1 
    return ans 

        