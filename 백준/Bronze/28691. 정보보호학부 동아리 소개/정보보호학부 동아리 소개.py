import sys

word = sys.stdin.readline().rstrip()

if word == "M":
    print("MatKor")
elif word == "W":
    print("WiCys")
elif word == "C":
    print("CyKor")
elif word == "A":
    print("AlKor")
else:
    print("$clear")
