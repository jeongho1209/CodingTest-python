while True:
    palindrome = input()

    if palindrome == '0':
        break

    if palindrome == palindrome[::-1]:
        print('yes')
    else:
        print('no')
