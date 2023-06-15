def solution(my_string):
    
    table = my_string.maketrans({
        'a' : "",
        'e' : "",
        'i' : "",
        'o' : "",
        'u' : ""
    })
            
    return my_string.translate(table)