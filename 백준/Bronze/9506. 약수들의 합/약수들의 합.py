while True:
    n = int(input())

    divisors = []

    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    if sum(divisors) == n:
        print(n, " = ", " + ".join(str(i) for i in divisors), sep="")
    else:
        print(n, "is NOT perfect.")
