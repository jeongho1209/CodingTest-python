import sys

target = [
    'Never gonna give you up',
    'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop'
]

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    t = sys.stdin.readline().rstrip()

    if t not in target:
        print('Yes')
        exit()

print('No')
