import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

pokemon = {}

for i in range(n):
    pokemon[i + 1] = sys.stdin.readline().rstrip()

reverse_dict = dict(map(reversed, pokemon.items()))

for i in range(m):
    answer = sys.stdin.readline().rstrip()
    try:
        answer = int(answer)
    except:
        print(reverse_dict[answer])
    else:
        print(pokemon[answer])
