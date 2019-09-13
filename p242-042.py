def salByDay1(sal):
    for days in range(1, 31):
        print(str(days).rjust(2), ':', "{:,}".format(sal).rjust(11))
        sal = sal * 2


def salByDay2(days, sal):
    if days < 31:
        print(str(days).rjust(2), ':', "{:,}".format(sal).rjust(11))
        return salByDay2(days + 1, sal * 2)

    return

if __name__ == "__main__":
    salByDay1(1)
    salByDay2(1, 1)
