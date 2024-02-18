import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    k = int(sys.stdin.readline().rstrip())

    words = []

    ans = 0

    for _ in range(k):
        words.append(sys.stdin.readline().rstrip())

    for i in range(k):
        for j in range(i, k):
            if i != j:
                word1 = words[i] + words[j]
                word2 = words[j] + words[i]
                if word1 == word1[::-1]:
                    ans = word1
                    break
                if word2 == word2[::-1]:
                    ans = word2
                    break

    print(ans)
