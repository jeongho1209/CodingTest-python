from itertools import combinations

def solution(number):
    comb = list(combinations(number, 3))
    
    answer = 0
    
    for i in comb:
        if sum(i) == 0:
            answer += 1
            
    return answer