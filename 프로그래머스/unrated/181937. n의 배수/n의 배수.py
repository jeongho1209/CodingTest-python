def solution(num, n):
    if num % n == 0:
        return 1
    elif num % n != 0:
        return 0