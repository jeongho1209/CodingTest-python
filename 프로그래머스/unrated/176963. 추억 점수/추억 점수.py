def solution(name, yearning, photo):
    score_dict = dict(zip(name, yearning))
    
    ans = 0
    answer = []
            
    for people in photo:
        for person in people:
            if person in score_dict.keys():
                ans += score_dict[person]
        answer.append(ans)
        ans = 0
    
    return answer