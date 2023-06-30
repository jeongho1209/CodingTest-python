def solution(lottos, win_nums):
    # lottos -> 가려진 로또 종이
    # win_nums -> 로또 당첨 번호
    answer = []
    cnt = 0
    zero_cnt = 0
    
    for num in lottos:
        if num == 0:
            zero_cnt += 1
        for win_num in win_nums:
            if num == win_num:
                cnt += 1
    
    max_lotto = zero_cnt + cnt
    min_lotto = cnt
    
    if max_lotto == 6:
        answer.append(1)
    elif max_lotto == 5:
        answer.append(2)
    elif max_lotto == 4:
        answer.append(3)
    elif max_lotto == 3:
        answer.append(4)
    elif max_lotto == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    if min_lotto == 6:
        answer.append(1)
    elif min_lotto == 5:
        answer.append(2)
    elif min_lotto == 4:
        answer.append(3)
    elif min_lotto == 3:
        answer.append(4)
    elif min_lotto == 2:
        answer.append(5)
    else:
        answer.append(6)

    return answer