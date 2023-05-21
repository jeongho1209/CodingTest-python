def solution(num_list):
    answer = []
    for index in num_list:
        if index < 0:
            answer.append(index)
            
    if not answer:
        return -1
    else:
        return num_list.index(answer[0])