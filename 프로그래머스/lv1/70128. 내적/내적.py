def solution(a, b):
    
    answer = []
    
    sum = 0
    
    for i in a:
        answer.append(i)
        
    for j in b:
        answer.append(j)
    
    for i in range(0, len(a)):
        sum += answer[i] * answer[len(a) + i]
    
    return sum