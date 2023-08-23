n, m = map(int, input().split())

notListenPeople = set()
notSeePeople = set()

answer = []

for i in range(n):
    notListenPeople.add(input())

for j in range(m):
    notSeePeople.add(input())

answer = notListenPeople & notSeePeople

answer = sorted(list(answer))

print(len(answer))
for i in answer:
    print(i)
