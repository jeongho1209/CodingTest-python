# 1. cities 순회하면서 caches 배열에 존재하면 +1, 존재하지 않으면 +5 처리
# 2. caches 배열에 담기 위해서 계속 append하는데 cachesize보다 길으면 popleft함

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    new_cities = []
    
    caches = deque(maxlen=cacheSize)
    
    for c in cities:
        new_cities.append(c.upper())
    
    for c in new_cities:
        if c in caches:
            caches.remove(c)
            caches.append(c)
            answer += 1
        else:
            caches.append(c)
            answer += 5
        
    return answer