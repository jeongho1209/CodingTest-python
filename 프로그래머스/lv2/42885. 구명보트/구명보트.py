def solution(people, limit):
    cnt = 0
    start, end = 0, len(people) - 1
    people.sort()
    
    while start <= end:
        if people[start] + people[end] <= limit: 
            start += 1
        end -= 1
        cnt += 1
    return cnt