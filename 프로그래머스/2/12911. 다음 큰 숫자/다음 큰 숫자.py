# 1. n보다 큰 자연수
# 2. bin(n) == bin(다음 큰 숫자) -> 1의 개수가 같음(1의 위치만 옮기는듯)
# 3. 1, 2 만족하면서 가장 작은 수
# n부터 for문 하나 돌면서 bin 바꿔보고 1 개수 같으면 answer이고 break

def solution(n):
    answer = 0

    count_n = bin(n).count('1')

    for i in range(n + 1, 10000 ** 2):
        target = bin(i)[2:]
        if target.count('1') == count_n:
            answer = target
            break

    return int(answer, 2)