import sys

N = int(sys.stdin.readline().rstrip())
cranes = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
boxs = list(map(int, sys.stdin.readline().rstrip().split()))

cranes.sort(reverse=True)
boxs.sort(reverse=True)

if cranes[0] < boxs[0]:
    print(-1)
    exit()

time = 0

while boxs:
    for crane in cranes:
        for box in boxs:
            if crane >= box:
                boxs.remove(box)
                break
    time += 1

print(time)
