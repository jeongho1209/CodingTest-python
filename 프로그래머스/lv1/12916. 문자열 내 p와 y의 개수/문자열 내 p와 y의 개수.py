def solution(s):
    answer = True
    
    sCount = s.count('y')
    SCount = s.count('Y')
    pcount = s.count('p')
    PCount = s.count('P')

    if sCount + SCount == pcount + PCount:
        answer = True
    else:
        answer = False
    
    return answer