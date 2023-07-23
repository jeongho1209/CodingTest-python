def solution(a, b, c):
    SUM = a + b + c
    Multiple = a * a + b * b + c * c
    Multiple3 = a * a * a + b * b * b + c * c * c
    
    if a != b and b != c and a != c:
        return SUM
    elif a == b and b != c or a == c and b != a or b == c and a != c:
        return SUM * Multiple
    elif a == b and b == c:
        return SUM * Multiple * Multiple3