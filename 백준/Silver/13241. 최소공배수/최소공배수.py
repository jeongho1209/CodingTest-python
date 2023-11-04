import math
import sys

A, B = map(int, sys.stdin.readline().rstrip().split())

print(A * B // math.gcd(A, B))
