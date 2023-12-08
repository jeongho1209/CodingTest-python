def solution(k, score):
    answer = []
    
    legends = []
    
    for i, v in enumerate(score):
        if i + 1 <= k:
            legends.append(v)
        else:
            if min(legends) < v:
                legends.remove(min(legends))
                legends.append(v)
        answer.append(min(legends))
    
    return answer