p = int(input())

soft = 0
hard = 0
ai = 0
first = 0

for i in range(p):
    grade, classNum, number = map(int, input().split())

    if grade == 1:
        first += 1
    else:
        if classNum == 1 or classNum == 2:
            soft += 1
        elif classNum == 3:
            hard += 1
        else:
            ai += 1

print(soft)
print(hard)
print(ai)
print(first)