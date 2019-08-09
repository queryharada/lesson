#
# 素数とは 1または自分自身以外で割り切れない整数のこと
# 抽出した素数を保存しておき、この素数で割り切れない数が素数である。
#

# 抽出した素数の配列：最小数素数の2を設定
pnArray = [2]
# 抽出する最大値
maxNumber = 10000
# 3からmaxNumberまでを確かめる
for chkNumber in range(3, maxNumber):
    # チェックフラグ初期化
    pnChk = True
    # 今まで抽出した素数で割れるかチェック
    for pnNumber in pnArray:
        # 割り切れたら素数でない
        if (chkNumber % pnNumber) == 0:
            pnChk = False
    # 今まで抽出した素数で割り切れないので素数である。
    if pnChk == True:
        # 素数として配列に追加
        pnArray.append(chkNumber)

# 抽出した素数表示
line = ""
for pnNumber in pnArray:
    line = line + repr(pnNumber).rjust(len(str(maxNumber)))
    if len(line) > 80:
        print(line)
        line = ""
