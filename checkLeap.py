# -*- coding:utf-8 -*-

def check_leap_year(year):
    """ 閏年判定 """
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def main():
    """ エントリーポイント """
    years = [2016, 2000, 1990, 1980]

    for year in years:
        if check_leap_year(year):
            print(str(year) + "年は閏年です。")
        else:
            print(str(year) + "年は平年です。")


if __name__ == "__main__":
    main()
