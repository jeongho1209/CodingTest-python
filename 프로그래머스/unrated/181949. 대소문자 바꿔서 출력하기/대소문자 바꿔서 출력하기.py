str = input()

newStr = []

for i in str:
    if i.islower():
        newStr.append(i.upper())
    else:
        newStr.append(i.lower())
        
print(''.join(newStr))