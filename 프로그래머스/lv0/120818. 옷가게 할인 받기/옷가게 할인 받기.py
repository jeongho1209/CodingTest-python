def solution(price):
    if price >= 500000:
        free = 20
    elif price >= 300000:
        free = 10
    elif price >= 100000:
        free = 5
    elif price < 100000: 
        free = 0
    return int(price - price * (free / 100))