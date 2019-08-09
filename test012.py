# -*- coding: utf-8 -*-
# bubble_sort.py
def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
    return arr


# sellect_sort.py
def sellect_sort(arr):
    for ind, ele in enumerate(arr):
        min_ind = min(range(ind, len(arr)), key=arr.__getitem__)
        arr[ind], arr[min_ind] = arr[min_ind], ele
    return arr


# insert_sort.py
def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        ele = arr[i]
        while arr[j] > ele and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = ele
    return arr


# nsert_sort_bin.py
import sys

sys.setrecursionlimit(10 ** 7)


def binary_search(arr, low, hig, ele):
    if low == hig:
        if arr[low] > ele:
            return low
        else:
            return low + 1
    elif low > hig:
        return low

    mid = (low + hig) // 2
    if arr[mid] < ele:
        return binary_search(arr, mid + 1, hig, ele)
    elif arr[mid] > ele:
        return binary_search(arr, low, mid - 1, ele)
    else:
        return mid


#
def insert_sort_bin(arr):
    for i in range(1, len(arr)):
        ele = arr[i]
        ind = binary_search(arr, 0, i - 1, ele)
        arr[:] = arr[:ind] + [ele] + arr[ind:i] + arr[i + 1:]
    return arr

# insert_sort_bin_buildin.py
# import bisect
# def insert_sort_bin_buildin(arr):
#    for i in range(1, len(arr)):
#        bisect.insort(arr, arr.pop(i), 0, i)
#    return arr


# merge_sort.py
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # ここで分割を行う
    left = arr[:mid]
    right = arr[mid:]

    # 再帰的に分割を行う
    left = merge_sort(left)
    right = merge_sort(right)

    # returnが返ってきたら、結合を行い、結合したものを次に渡す
    return merge(left, right)


#
def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged


# quick_sort.py
def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    # データの状態に左右されないためにrandom.choice()を用いることもある。
    # ref = random.choice(arr)
    ref = arr[0]
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right


# count_sort.py
def count_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    count = [0] * (max_num - min_num + 1)
    for ele in arr:
        count[ele - min_num] += 1

    return [ele for ele, cnt in enumerate(count, start=min_num) for __ in range(cnt)]


def main():
    pass


if __name__ == "__main__":
    main()
