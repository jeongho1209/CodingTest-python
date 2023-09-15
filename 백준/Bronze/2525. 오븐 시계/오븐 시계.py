A, B = map(int, input().split())

C = int(input())

M = A * 60 + B + C

if M >= 1440:
    M -= 1440

answerA = M // 60
answerB = M % 60

print(answerA, answerB)
