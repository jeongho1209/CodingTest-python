import sys

N, K, P = map(int, sys.stdin.readline().rstrip().split())
bread = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0

for b in range(0, len(bread), K):
    cnt = sum(bread[b: b + K])  # 크림빵 개수
    if cnt >= P:  # 크림빵 개수가 P개 이상 -> 판매 가능
        ans += 1

print(ans)
