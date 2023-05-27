def solution(price, money, count): 
    for i in range(1, count + 1):
        money -= i * price
        
    if money >= 0:
        money = 0
    else:
        money *= -1

    return money