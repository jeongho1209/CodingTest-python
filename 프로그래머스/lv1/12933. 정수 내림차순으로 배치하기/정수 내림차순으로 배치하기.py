def solution(n):
    answer = []
    
    for index in reversed(sorted(list(map(int, str(n))))):
        answer.append(str(index))
    
    return int(''.join(answer))