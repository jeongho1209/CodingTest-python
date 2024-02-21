import sys

n = int(sys.stdin.readline().rstrip())

students = []
stu_dict = {}

for _ in range(n):
    nation_num, stu_num, score = map(int, sys.stdin.readline().rstrip().split())
    students.append((nation_num, stu_num, score))

    if nation_num not in stu_dict:
        stu_dict[nation_num] = 0

students.sort(reverse=True, key=lambda x: x[2])

cnt = 0

for nation_num, stu_num, _ in students:
    if cnt == 3:
        exit()
    else:
        stu_dict[nation_num] += 1
        if stu_dict[nation_num] > 2:
            continue
        else:
            print(nation_num, stu_num)
            cnt += 1
