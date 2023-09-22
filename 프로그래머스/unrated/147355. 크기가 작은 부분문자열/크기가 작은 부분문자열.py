# t[index:len(p)]

def solution(t, p):
    answer = []
    newAnswer = []
    cnt = 0
    value = ''
    
    for i in range(len(t)):
        value = t[i : len(p) + i]  # 인덱스마다 파싱
        answer.append(value)
        value = ''
        
    for i in answer:  # 길이만큼으로 파싱
        if len(i) == len(p) and i <= p:
            cnt += 1
    
    return cnt