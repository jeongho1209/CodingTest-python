import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())

food_a = {}
food_b = {}
food_c = set()

for _ in range(A):
    menu, price = sys.stdin.readline().rstrip().split()
    food_a[menu] = int(price)

for _ in range(B):
    menu, price = sys.stdin.readline().rstrip().split()
    food_b[menu] = int(price)

for _ in range(C):
    food_c.add(sys.stdin.readline().rstrip())

N = int(sys.stdin.readline().rstrip())

orders = []

for _ in range(N):
    orders.append(sys.stdin.readline().rstrip())

answer = "Okay"

common, special, service = 0, 0, 0

for o in orders:
    if o in food_a:
        common += food_a[o]

    if o in food_b:
        special += food_b[o]

    if o in food_c:
        service += 1

if common < 20000 and special > 0:
    answer = "No"
else:
    if common + special < 50000 and service > 0:
        answer = "No"
    elif service > 1:
        answer = "No"

print(answer)
