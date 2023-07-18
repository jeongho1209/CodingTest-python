def solution(todo_list, finished):
    answer = []
    
    for k, v in zip(todo_list, finished):
        if v == False:
            answer.append(k)
    
    return answer