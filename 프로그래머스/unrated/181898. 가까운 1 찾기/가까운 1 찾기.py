def solution(arr, idx):
    answer = -1
    for i, num in enumerate(arr):
        if i >= idx and num == 1:
            return i
    return answer