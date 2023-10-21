import sys

_ = sys.stdin.readline()
arr = list(map(int, sys.stdin.readline().rstrip().split()))

newArr = sorted(list(set(arr)))

dic = {}
for i in range(len(newArr)):
    dic[newArr[i]] = i

for i in arr:
    print(dic[i], end=' ')
