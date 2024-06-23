_ = input()
arr = list(map(int, input().split()))

target = sum(arr)

if target >= 1:
    print('Right')
elif target <= -1:
    print('Left')
else:
    print('Stay')