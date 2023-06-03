def solution(s1, s2):
    Len = len(s1 + s2)
    dis = len(set(list(s1 + s2)))

    return Len - dis