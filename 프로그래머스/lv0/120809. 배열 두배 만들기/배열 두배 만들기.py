def solution(numbers):
    answer = []
    j = 0
    for i in numbers:
        answer.append(numbers[j] * 2)
        j += 1
    return answer