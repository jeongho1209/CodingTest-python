def solution(d, budget):
    answer = 0
    
    for pay in sorted(d):
        if budget - pay >= 0:
            budget -= pay
            answer += 1
            if budget < 0:
                answer -= 1
    return answer