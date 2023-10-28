import sys

while True:
    try:
        n, k = map(int, sys.stdin.readline().rstrip().split())
        chicken = n + (n // k)
        while n >= k:
            n = (n // k) + (n % k)
            chicken += n // k
        print(chicken)
    except:
        exit()
