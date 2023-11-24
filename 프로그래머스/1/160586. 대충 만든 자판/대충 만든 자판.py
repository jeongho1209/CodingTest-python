def solution(keymap, targets):
    answer = []

    for target_list in targets:
        score = 0
        for real_target in target_list:
            target_index = []
            for k in keymap:
                if real_target in k:
                    target_index.append(k.index(real_target) + 1)
            try:
                score += min(target_index)
            except:
                score = -1
                break
        answer.append(score)

    return answer
