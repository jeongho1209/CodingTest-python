import sys, re


def get_lens(string):
    string = re.sub(r"[^a-z]", '', string.lower())

    alphabets = list(set(string))

    return len(alphabets)


while True:
    answer = sys.stdin.readline().rstrip()

    if answer == '#':
        break

    print(get_lens(answer))
