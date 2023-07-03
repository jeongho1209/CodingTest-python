def solution(num_list):
    answerM = 1
    answerS = sum(num_list) ** 2
    
    for i in num_list:
        answerM *= i
        
    if answerM < answerS:
        return 1
    else:
        return 0