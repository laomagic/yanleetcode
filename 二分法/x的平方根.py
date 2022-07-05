# coding:utf-8
"""
题目：
    给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
    由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
"""


def mySqrt(x):
    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 == x:
            return mid
        elif mid ** 2 < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


if __name__ == '__main__':
    result = mySqrt(34)
    print(result)
