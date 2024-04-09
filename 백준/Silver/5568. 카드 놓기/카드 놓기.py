import sys

n = int(sys.stdin.readline().rstrip())

k = int(sys.stdin.readline().rstrip())

cards = []

ans = set()

visited = [False] * n

for _ in range(n):
    cards.append(int(sys.stdin.readline().rstrip()))


def dfs(depth, value):
    if depth == k:
        ans.add(value)
        return
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(depth + 1, value + str(cards[i]))
                visited[i] = False


dfs(0, '')

print(len(ans))
