import sys

L, C = map(int, sys.stdin.readline().rstrip().split())

input_arr = list(sys.stdin.readline().rstrip().split())

arr = []

for i in input_arr:
    arr.append((i, ord(i)))

arr.sort(key=lambda x: x[0])

ans = []

vowels = ['a', 'e', 'i', 'o', 'u']


def check():
    vowels_count = 0
    consonants_count = 0

    for value in ans:
        if value in vowels:
            vowels_count += 1
        else:
            consonants_count += 1

    if vowels_count >= 1 and consonants_count >= 2:
        return True
    else:
        return False


def dfs(value_idx):
    if len(ans) == L:
        if check():
            print(''.join(map(str, ans)))
        return

    for index in range(value_idx, C):
        if arr[index][0] not in ans:
            ans.append(arr[index][0])
            dfs(index + 1)
            ans.pop()


dfs(0)
