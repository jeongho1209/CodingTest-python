burger = []
juice = []

for i in range(5):
    if i <= 2:
        burger.append(int(input()))
    else:
        juice.append(int(input()))

print(min(burger) + min(juice) - 50)