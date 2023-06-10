def solution(k, m, score):
    score.sort()

    sum = 0
    
    for i in range(len(score), m-1, -m):
        sum += score[i -m ] * m
        
    return sum