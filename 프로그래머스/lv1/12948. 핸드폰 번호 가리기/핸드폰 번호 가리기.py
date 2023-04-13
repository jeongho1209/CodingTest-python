def solution(phone_number):
    answer = phone_number[-4:]
    blind = ""
    leng = len(phone_number) - 4
    for i in range(leng):
        blind += "*"
    return blind + answer