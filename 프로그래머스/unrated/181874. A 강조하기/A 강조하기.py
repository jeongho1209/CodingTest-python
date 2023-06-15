def solution(myString):
    answer = []
    for i in myString:
        if i == 'a' or i == 'A':
            answer.append(i.upper())
        else:
            answer.append(i.lower())
    return "".join(answer)