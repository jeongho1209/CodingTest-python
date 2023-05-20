def solution(n):
    result = []
    for i in range(1, n):
        if n % i == 1:
            result.append(i)
    return result[0]

