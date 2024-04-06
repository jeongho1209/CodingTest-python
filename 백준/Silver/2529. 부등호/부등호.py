import sys

k = int(sys.stdin.readline().rstrip())

arr = list(sys.stdin.readline().rstrip().split())

max_ans = ''
min_ans = ''

visited = [0] * 10


def check(i, j, o):
    if o == '<':
        return i < j
    else:
        return i > j


def dfs(depth, value):
    global min_ans, max_ans
    if depth == k + 1:
        if min_ans == '':
            min_ans = value
        else:
            max_ans = value
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(value[-1], str(i), arr[depth - 1]):
                visited[i] = True
                dfs(depth + 1, value + str(i))
                visited[i] = False


dfs(0, '')

print(max_ans)
print(min_ans)
