import sys

t = int(sys.stdin.readline().rstrip())


def binary_search(start, end, note1, target):
    while start <= end:
        mid = (start + end) // 2

        if note1[mid] == target:
            return 1
        elif note1[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for _ in range(t):
    answer = []

    _ = int(sys.stdin.readline().rstrip())
    note1 = list(map(int, sys.stdin.readline().rstrip().split()))
    note1.sort()

    _ = int(sys.stdin.readline().rstrip())
    note2 = list(map(int, sys.stdin.readline().rstrip().split()))

    for target in note2:
        answer.append(binary_search(0, len(note1) - 1, note1, target))

    for i in answer:
        print(i)
