def solution(a, b):
    answer1 = str(a) + str(b)
    answer2 = str(b) + str(a)
    
    if int(answer1) > int(answer2):
        return int(answer1)
    elif int(answer1) < int(answer2):
        return int(answer2)
    else:
        return int(answer1)