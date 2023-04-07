import re

def solution(my_string):
    answer = 0
    for i in re.findall(r'\d', my_string):
        answer += int(i)
    return answer