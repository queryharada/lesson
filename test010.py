def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


n = 8
for i in range(1, n):
    print(fact(i))
