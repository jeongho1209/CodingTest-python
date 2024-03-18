import sys

H = sys.stdin.readline().rstrip()
N = sys.stdin.readline().rstrip()

H = H.replace(N, '3')

print(H.count('3'))
