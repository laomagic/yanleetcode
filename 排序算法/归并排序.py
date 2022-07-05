# coding:utf-8
"""
归并排序：
    归并排序运用分治递归思想：将大问题分为较小的子问题，分而治之；递归调用同样的方法解决子问题。
    最终将序列的排序问题分治为一个数的排序问题，关键在于如何将子问题答案合并为问题答案。
"""


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    index = len(nums) // 2
    left = nums[:index]
    right = nums[index:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    """元素合并"""
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # 添加剩余元素
    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    nums = [1, 34, 2, 100, 3, 10, 4, 20, 10, 200]
    result = merge_sort(nums)
    print(result)
