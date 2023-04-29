def solution(n):
    solve = []
    answer = list(map(int, str(n)))
    for i in reversed(answer):
        solve.append(i)
    return solve