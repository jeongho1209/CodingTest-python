# 1. while(s == '1')
# 2. s돌면서 0만나면 0 지우고 cnt에 더하기
# 3. 0 제거후 길이 갖고 새로운 문자열 만들기

def solution(s):
    zeroCnt = 0
    changeTwo = 0
    
    while(s != '1'):
        for i in s:
            if i == '0':
                s = s.replace('0', '')
                zeroCnt += 1
        s = format(len(s), 'b')
        changeTwo += 1
        
    return changeTwo, zeroCnt