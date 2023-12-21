import sys

n = int(sys.stdin.readline().rstrip())

if 380 <= n < 425:
    print('Violet')
elif 425 <= n < 450:
    print('Indigo')
elif 450 <= n < 495:
    print('Blue')
elif 495 <= n < 570:
    print('Green')
elif 570 <= n < 590:
    print('Yellow')
elif 590 <= n < 620:
    print('Orange')
else:
    print('Red')
   