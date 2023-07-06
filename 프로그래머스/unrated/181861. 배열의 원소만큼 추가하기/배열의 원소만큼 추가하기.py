def solution(arr):
    answer = []
    
    for i in arr:
        for j in range(1, i+1):
            answer.append(i)
    
    return answer