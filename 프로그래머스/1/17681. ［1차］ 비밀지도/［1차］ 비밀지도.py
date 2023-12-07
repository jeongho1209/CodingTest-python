def solution(n, arr1, arr2):
    answer = []
    
    for i1, i2 in zip(arr1, arr2):
        answer.append(bin(i1 | i2)[2:].zfill(n).replace('1', '#').replace('0', ' '))
    
    return answer