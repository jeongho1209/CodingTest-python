# 1. 약수 개수 먼저 구하기
  # 1.1 -> n이면 1 ~ n // 2까지 돌면서 약수일때마다 수 더하기 n + 1마다 수 초기화
  # 
# 2. measure[i] > limit -> measure[i] = power

def solution(number, limit, power):
    measures = [] # 약수 담는 배열
    
    for i in range(2, number + 1):
        measure = 0
        for j in range(1, int(i ** (1/2) + 1)):
            if i % j == 0:
                measure += 1
                if j ** 2 != i:
                    measure += 1
        if measure > limit:
            measure = power
        measures.append(measure)
    
    return sum(measures) + 1