# a개 주면 -> b만큼 준다. 갖고 있는건 n만큼이다
# 콜라 개수 -= 준개수 + 받은 개수
def solution(a, b, n):
    answer = 0
    
    while(n >= a):
        n = n + b - a
        answer += b
    
    return answer