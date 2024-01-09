import sys

# A는 B를 먹음 A > B보다 큰게 어떤게 있는지 찾기
# A배열 for문 하나 돌면서 각 값에 B 배열(정렬 필요)이랑 이분 탐색 돌림
# 이분 탐색 ->

T = int(sys.stdin.readline().rstrip())


def binary_search(target):
    s, e = 0, len(live_b) - 1

    res = -1

    while s <= e:
        mid = (s + e) // 2

        if live_b[mid] < target:
            res = mid
            s = mid + 1
        else:
            e = mid - 1

    return res


for _ in range(T):
    _ = sys.stdin.readline()

    ans = 0

    live_a = list(map(int, sys.stdin.readline().rstrip().split()))
    live_b = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

    for a in live_a:
        ans += binary_search(a) + 1

    print(ans)
