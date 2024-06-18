answer = 0


def dfs(idx, t, nums, target):
    global answer

    if idx == len(nums):
        if t == target:
            answer += 1
    else:
        dfs(idx + 1, t + nums[idx], nums, target)
        dfs(idx + 1, t - nums[idx], nums, target)


def solution(numbers, target):
    dfs(0, 0, numbers, target)

    return answer
