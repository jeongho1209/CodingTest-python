# A, B 배열 둘 다 정렬을 한 뒤
# A[0] * B[len(B) - 1] -> A는 다음 인덱스가고 B는 이전 인덱스로 온다
def solution(A,B):
    sortedA = sorted(A)
    sortedB = sorted(B)
    answer = 0
    cnt = 0
    a = 0
    b = len(B) - 1
    
    while(cnt <= len(A) - 1):
        answer += sortedA[a] * sortedB[b]
        a += 1
        b -= 1
        cnt += 1
        
    return answer