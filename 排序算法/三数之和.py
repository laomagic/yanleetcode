# coding:utf-8
"""
题目：给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
做法：先排序，后双指针
"""


def three_sum(nums):
    # 排序
    nums.sort()
    result = set()
    k = 0
    for k in range(len(nums) - 2):
        if nums[k] > 0:
            break
        i, j = k + 1, len(nums) - 1
        while i < j:
            s = nums[i] + nums[k] + nums[j]
            if s < 0:
                i += 1
            elif s > 0:
                j -= 1
            else:
                result.add((nums[k], nums[i], nums[j]))
                i += 1
                j -= 1
    return list(result)


if __name__ == '__main__':
    nums = [-6, -3, -2, -5, -5, 0, 5, 6, 8]
    result = three_sum(nums)
    print(result)
