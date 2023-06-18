def solution(n):
    answer = 0
    odd = 1
    even = 2
    if n % 2 != 0: # n이 홀수
        while odd <= n:
            answer += odd
            odd += 2
    else:
        while even <= n:
            answer += even ** 2
            even += 2
            
    return answer