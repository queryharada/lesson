def Fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)


def main():
    print(Fib(10))


#    print([Fib(n) for n in range(1, 10)])


if __name__ == "__main__":
    main()
