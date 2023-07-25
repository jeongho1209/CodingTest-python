def solution(num_list):
    answer1 = 0
    answer2 = 0
    
    for k, v in enumerate(num_list):
        if k % 2 == 0:
            answer1 += v
        else:
            answer2 += v
    
    if answer1 > answer2:
        return answer1
    elif answer2 > answer1:
        return answer2
    else:
        return answer1