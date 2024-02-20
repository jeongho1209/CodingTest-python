import sys

n = int(sys.stdin.readline().rstrip())

alphabets = list(sys.stdin.readline().rstrip())

alpha_dict = {}

for a in alphabets:
    if a not in alpha_dict:
        alpha_dict[a] = 1
    else:
        alpha_dict[a] += 1

alpha_list = sorted(list(alpha_dict.items()), key=lambda x: x[1], reverse=True)

for k, v in alpha_list:
    if k != ' ' and k != '.' and k != ',':
        print(v)
        exit()
