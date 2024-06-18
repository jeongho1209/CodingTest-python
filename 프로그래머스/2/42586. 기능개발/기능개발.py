def solution(progresses, speeds):
    answer = []
    
    time = 1
    
    cnt = 0

    while progresses:
        if progresses[0] + time * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt >= 1:
                answer.append(cnt)
                cnt = 0
            time += 1
    
    answer.append(cnt)

    return answer
