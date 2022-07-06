# coding:utf-8
"""
题目：
    给你 旋转后 的数组 nums 和一个整数 target ，
    如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
"""


def search_matrix(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return nums[mid]
        # 左半段有序
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 有半段有序
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

    pass


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 5
    result = search_matrix(nums, target)
    print(result)
