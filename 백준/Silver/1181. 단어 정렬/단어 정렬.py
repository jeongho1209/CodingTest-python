charList = []

N = int(input())

for _ in range(N):
    charList.append(input())

newCharList = list(set(charList))
newCharList.sort()
newCharList.sort(key=len)

for char in newCharList:
    print(char)