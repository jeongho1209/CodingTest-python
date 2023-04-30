def solution(x):
    sum = 0
    answer = True
    
    for i in list(map(int, str(x))):
        sum += i
    
    if(x % sum == 0):
        answer = True
    else:
        answer = False
    
    return answer