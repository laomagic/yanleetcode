# coding:utf-8
"""
冒泡排序：
    1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    2.对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
    3.针对所有的元素重复以上的步骤，除了最后一个
"""


def bubble_sort(nums):
    length = len(nums)
    for i in range(0, length):
        for j in range(0, length-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(nums)
    pass


if __name__ == '__main__':
    nums = [5, 3, 2, 10, 1, 200, 500, 10, 20, 3, 34, 20, 2000]
    bubble_sort(nums)
