def solution(absolutes, signs):
    SUM = 0

    for k,v in zip(absolutes, signs):
        if v == False:
            SUM -= k
        elif v == True:
            SUM += k
            
    return SUM