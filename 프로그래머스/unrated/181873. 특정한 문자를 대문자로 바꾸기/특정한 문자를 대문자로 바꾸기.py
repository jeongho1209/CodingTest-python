def solution(my_string, alp):
    answer = ''
    
    for st in my_string:
        if st == alp:
            my_string = my_string.replace(alp, st.upper())
    return my_string