import sys

while True:
    target = int(sys.stdin.readline().rstrip())

    if target == 0:
        break

    if target % 42 == 0:
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")
