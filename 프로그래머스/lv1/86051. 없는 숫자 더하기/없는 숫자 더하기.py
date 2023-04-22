def solution(numbers):
    num = 0
    for index in range(10):
        if index not in numbers:
            num += index
    return num
