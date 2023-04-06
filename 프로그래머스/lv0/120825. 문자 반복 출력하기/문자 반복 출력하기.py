def solution(my_string, n):
    answer = []
    for i in range(len(my_string)):
        for j in range(n):
            answer.append(my_string[i])
    return ''.join(answer)