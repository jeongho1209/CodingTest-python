def solution(arr):
    answer = arr.index(min(arr))
    arr.pop(answer)
    
    if len(arr) == 0:
        arr.append(-1)
    
    return arr
