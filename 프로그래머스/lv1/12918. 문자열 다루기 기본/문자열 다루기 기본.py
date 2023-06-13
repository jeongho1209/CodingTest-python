def solution(s):
    answer = s.isdigit()
    
    if len(s) == 4 or len(s) == 6:
        if answer == True:
            return True
        else:
            return False
    else:
        return False
