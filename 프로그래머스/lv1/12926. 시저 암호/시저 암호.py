# 소문자면 90 넘었을 때 26 빼기
# 대문자면 122 넘었을 때 26 빼기
def solution(s, n):
    answer = ''
    for i in s:
        if i != ' ': # 문자열 경우
            if 65 <= ord(i) <= 90:
                caesar = (chr(ord(i) + n))
                if ord(caesar) > 90:
                    caesar = chr(ord(caesar) - 26)        
            elif 97 <= ord(i) <= 122:
                caesar = (chr(ord(i) + n))
                if ord(caesar) > 122:
                    caesar = chr(ord(caesar) - 26)    
            answer += caesar
        else: # 공백일 경우 그냥 처리
            answer += i
    return answer