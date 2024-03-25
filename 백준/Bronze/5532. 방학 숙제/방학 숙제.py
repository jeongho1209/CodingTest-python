import sys

L = int(sys.stdin.readline().rstrip())
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())

v1 = 0
v2 = 0

if A % C == 0:
    v1 = A // C
else:
    v1 = A // C + 1

if B % D == 0:
    v2 = B // D
else:
    v2 = B // D + 1

print(L - max(v1, v2))
