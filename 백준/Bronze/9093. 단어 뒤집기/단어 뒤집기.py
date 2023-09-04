t = int(input())

for _ in range(t):
    answer = ''
    sentence = input().split()

    for i in range(len(sentence)):
        if i > 0:
            answer += ' '
            answer += sentence[i][::-1]
        else:
            answer += sentence[i][::-1]

    print(answer)
