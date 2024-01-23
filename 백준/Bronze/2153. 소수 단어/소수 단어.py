import math

ans = 0

for i in input():
    if i.islower():
        ans += ord(i) - 96
    else:
        ans += ord(i) - 38
       
isPrime = True
for i in range(2, int(math.sqrt(ans)) + 1):
    if ans % i == 0:
        isPrime = False

if isPrime:
    print('It is a prime word.')
else:
    print('It is not a prime word.')
