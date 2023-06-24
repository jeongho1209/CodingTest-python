def solution(num_list):
    
    SUM = 1
    
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for i in num_list:
            SUM *= i
        return SUM