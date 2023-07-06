def solution(num_list, n):
    answer = []
    
    for i in num_list:
        n -= 1
        if n >= 0:
            answer.append(i)
    
    return answer