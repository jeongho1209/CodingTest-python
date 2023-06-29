def solution(a, b):
    answer = 0
    
    if a % 2 != 0 and b % 2 != 0:
        answer += a * a + b * b
    elif a % 2 != 0 or b % 2 != 0:
        answer += (a + b) * 2
    else:
        if a - b < 0:
            answer += (a - b) * - 1
        else:
            answer += a - b
            
    return answer