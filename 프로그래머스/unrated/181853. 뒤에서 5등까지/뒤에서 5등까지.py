def solution(num_list):
    answer = []
    
    for i in sorted(num_list)[:5]:
        answer.append(i)
    
    return answer