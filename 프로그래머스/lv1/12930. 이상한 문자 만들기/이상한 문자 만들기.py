# split해서 담은 뒤 인덱스 % 2 == 0 -> upper else -> 소문자

def solution(s):
    answer = ''
    
    for i in s.split(" "):
        for index, value in enumerate(i):
            if index % 2 == 0:
                answer += value.upper()
            else:
                answer += value.lower()
        answer += ' '
    
    return answer[:-1]
