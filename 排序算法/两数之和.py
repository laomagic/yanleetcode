# coding:utf-8
"""
题目：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target
 的那 两个 整数，并返回它们的数组下标。
"""


def two_sum(nums, target):

    hashset = {}
    result = []
    for index, num in enumerate(nums):
        if target - nums[index] in hashset:
            result.append([index, hashset[target-nums[index]]])
        hashset[nums[index]] = index

    return result


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(result)
