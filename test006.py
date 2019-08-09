def MisteryWrite(LastP, CurrentP):
    if CurrentP < 100:
        print(CurrentP)
    Temp = CurrentP + LastP
    return Temp


def main():
    Last = 0
    Current = 1
    while Current < 100:
        Current = MisteryWrite(Last, Current)
    print(Current)


if __name__ == "__main__":
    main()
