def solution(num_list, n):
    answer = 0
    for index in num_list:
        if index == n:
            answer += 1
    
    if answer > 1:
        answer = 1
    
    return answer