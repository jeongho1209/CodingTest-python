import sys

alphabet = sys.stdin.readline().rstrip()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    alphabet = alphabet.replace(i, "*")

print(len(alphabet))
