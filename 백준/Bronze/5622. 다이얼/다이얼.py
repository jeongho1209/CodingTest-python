s = input()

diar = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

result = 0

for i in s:
    for j in diar:
        if i in j:
            result += diar.index(j) + 3

print(result)
