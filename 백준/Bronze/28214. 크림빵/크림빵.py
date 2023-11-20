import sys

N, K, P = map(int, sys.stdin.readline().rstrip().split())
bread = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0

for b in range(0, len(bread), K):
    cnt = K - sum(bread[b: b + K])  # 크림빵 없는 것 개수
    if cnt < P:  # 크림빵 없는 것 개수가 P개 미만 -> 판매 가능
        ans += 1

print(ans)
