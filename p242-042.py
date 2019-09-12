def salByDay1(sal):
    for i in range(1, 31):
        print(i, ':', sal)
        sal = sal * 2


def salByDay2(days, sal):
    if days > 30:
        return

    print(days, ':', sal)
    salByDay2(days + 1, sal * 2)


if __name__ == "__main__":
    salByDay1(1)
    salByDay2(1, 1)
