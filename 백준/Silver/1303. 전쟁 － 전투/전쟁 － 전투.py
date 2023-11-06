import sys

sys.setrecursionlimit(10 ** 7)

width, height = map(int, sys.stdin.readline().rstrip().split())

war = [list(sys.stdin.readline().rstrip()) for _ in range(height)]

my_power = 0  # 내 병사 위력
enemy_power = 0  # 상대 병사 위력
my_dfs_count = 0
enemy_dfs_count = 0


def dfs(i, j, k):
    if i >= height or j >= width or i < 0 or j < 0 or k != war[i][j]:
        return 0

    if k == 'W':
        global my_dfs_count
        my_dfs_count += 1
        war[i][j] = 'A'
        dfs(i + 1, j, k)
        dfs(i, j + 1, k)
        dfs(i - 1, j, k)
        dfs(i, j - 1, k)
    elif k == 'B':
        global enemy_dfs_count
        enemy_dfs_count += 1
        war[i][j] = 'A'
        dfs(i + 1, j, k)
        dfs(i, j + 1, k)
        dfs(i - 1, j, k)
        dfs(i, j - 1, k)


for i in range(height):
    for j in range(width):
        if war[i][j] != 'A':
            dfs(i, j, war[i][j])
            my_power += my_dfs_count ** 2
            enemy_power += enemy_dfs_count ** 2
        my_dfs_count = 0
        enemy_dfs_count = 0

print(my_power, enemy_power)
