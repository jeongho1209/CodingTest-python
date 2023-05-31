def solution(n, m):
    answer = []
    
    mins = []
    
    maxs = []
    
    for i in range(1, m + 1):
        if n % i == 0 and m % i == 0:
            mins.append(i)
    
    answer.append(max(mins))
    
    answer.append(n * m / max(mins))
    
    return answer