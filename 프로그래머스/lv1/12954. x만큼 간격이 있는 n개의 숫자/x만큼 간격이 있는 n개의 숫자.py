def solution(x, n):
    answer = [x]
    for i in range(1, n):
        answer.append(x + answer[0])
        x += answer[0]
    return answer