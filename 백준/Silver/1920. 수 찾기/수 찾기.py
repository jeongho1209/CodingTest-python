import sys

N = int(sys.stdin.readline().rstrip())
A_arr = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())
target = list(map(int, sys.stdin.readline().rstrip().split()))

A_arr.sort()

for t in target:
    left = 0
    right = N - 1

    flag = False

    while left <= right:
        mid = (left + right) // 2

        if A_arr[mid] > t:
            right = mid - 1
        elif A_arr[mid] < t:
            left = mid + 1
        else:
            flag = True
            print(1)
            break

    if not flag:
        print(0)
