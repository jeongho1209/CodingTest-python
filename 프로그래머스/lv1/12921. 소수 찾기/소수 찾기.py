# 1. 2 -> n까지(i로) 반복문 돈다
# 2. 그중에 i가 소수라면 answer += 1

import math

def is_prime(n):
    for j in range(2, int(math.sqrt(n) + 1)):
        if n % j == 0:
            return False
    return True

def solution(n):
    answer = 0
    
    for i in range(2, n + 1):
        if is_prime(i):
            answer += 1
    
    return answer