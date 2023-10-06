import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    cnt = 1
    people = []
    N = int(sys.stdin.readline().rstrip())
    for _ in range(N):
        people.append(list(map(int, sys.stdin.readline().rstrip().split())))

    people.sort()

    success = people[0][1]

    for i in range(len(people)):
        if people[i][1] < success:
            success = people[i][1]
            cnt += 1

    print(cnt)