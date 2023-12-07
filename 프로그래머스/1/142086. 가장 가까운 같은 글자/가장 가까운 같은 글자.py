def solution(s):
    answer = []
    dic = {}
    
    for i, v in enumerate(s):
        if v not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[v])
        dic[v] = i
        
    return answer