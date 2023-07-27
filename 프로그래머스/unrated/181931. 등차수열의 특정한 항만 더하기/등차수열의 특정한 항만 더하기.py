def solution(a, d, included):
    trueIndex = []
    
    answer = 0
    
    for i in range(len(included)):
        if included[i] == True:
            trueIndex.append(i)
            
    for i in trueIndex:
        answer += a + d * i
        
    return answer