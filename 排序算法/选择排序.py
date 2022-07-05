# coding:utf-8
"""
选择排序：
    1.对数据操作n-1轮，每轮找出一个最大（小）值。
    2.操作指选择，即未排序数逐个比较交换，争夺最值位置，每轮将一个未排序位置上的数交换成已排序数，即每轮选一个最值。
"""


def select_sort(nums):
    length = len(nums)
    for i in range(0, length - 1):
        min_index = i
        for j in range(i + 1, length):
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            nums[min_index], nums[i] = nums[i], nums[min_index]
    print(nums)
    pass


if __name__ == '__main__':
    nums = [10, 34, 2, 1, 20, 30, 200, 5, 100, 101]
    select_sort(nums)
