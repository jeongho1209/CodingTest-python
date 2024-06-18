import itertools, math

ans = []


def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True 


def getNums(nums):
    for i in range(1, len(nums) + 1):
        target = list(itertools.permutations(nums, i))

        for t in target:
            ans.append(int(''.join(t)))

    return ans


def solution(numbers):
    answer = 0

    getNums(numbers)

    real_ans = list(set(ans))
    
    for a in real_ans:
        if isPrime(a) and a > 1:
            print(a)
            answer += 1

    return answer
