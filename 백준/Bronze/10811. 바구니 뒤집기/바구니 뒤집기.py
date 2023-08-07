N, M = map(int, input().split())

bucket = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    bucket[i - 1:j] = reversed(bucket[i-1:j])

print(' '.join(str(q) for q in bucket))
