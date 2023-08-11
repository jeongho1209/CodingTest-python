def solution(nums):
    choose = len(nums) // 2
    return min(choose, len(set(nums)))