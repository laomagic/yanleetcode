# coding:utf-8

"""
题目：
    以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
    请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

"""


def merge(nums):
    nums.sort(key=lambda x: x[0])

    result = []
    for num in nums:
        if not result or result[-1][1] < num[0]:
            result.append(num)
        else:
            result[-1][1] = max(result[-1][1], num[1])
    return result


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = merge(intervals)
    print(result)
