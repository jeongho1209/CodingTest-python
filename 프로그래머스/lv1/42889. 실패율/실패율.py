# 실패율 -> 스테이지 도달(아직 클리어 X) 수 / 스테이지 도달 수
# N -> 전체 스테이지 개수
# stages -> 사용자가 멈춰있는 스테이지 번호들들
# return -> 실패율 높은 스테이지부터 내림차순으로 스테이지 번호들들

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 정렬 -> 내 앞 + 나 / 전체 길이 

def solution(N, stages):
    
    failed = {}
    
    players = len(stages)
    
    clear = 0
    
    for i in range(1, N + 1):
        if players == 0:
            failed[i] = 0
        else:
            cnt = stages.count(i)
            failed[i] = cnt / players
            players -= cnt

    return sorted(failed, key=lambda x: failed[x], reverse=True)