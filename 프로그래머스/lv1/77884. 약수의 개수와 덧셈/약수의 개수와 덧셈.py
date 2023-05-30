def solution(left, right):
    answerSum = 0
    for i in range(left, right + 1):
        print(checkAnswer(i))
        if checkAnswer(i) % 2 != 0:
            answerSum -= i
        else:
            answerSum += i
    
    return answerSum * -1

def checkAnswer(answer):
    count = 0
    for i in range(1, answer):
        if answer % i == 0:
            count += 1
            
    return count
            