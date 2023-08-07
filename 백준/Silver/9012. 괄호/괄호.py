for a in range(int(input())):
    stack = []
    for i in input():
        if i == '(':
            stack.append(i) # '('면 그냥 더하기
        else:
            if stack: # ')' 일때 짝 맞으니까 원래 있던 '(' 빼기
                stack.pop()
            else:
                print('NO') # ')' 이 처음으로 들어오면 잘못된 괄호
                break # 어차피 아니니까 그냥 멈추기
    else:
        if not stack: # 다 비워졌으면 올바른 괄호
            print('YES')
        else: # '(' 괄호가 남아있으면 잘못된 괄호
            print('NO')