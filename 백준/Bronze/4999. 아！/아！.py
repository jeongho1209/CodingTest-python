import sys

jae = sys.stdin.readline().rstrip()
doctor = sys.stdin.readline().rstrip()

if len(jae) >= len(doctor):
    print('go')
else:
    print('no')
