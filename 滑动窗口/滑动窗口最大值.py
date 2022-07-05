# coding:utf-8

"""
题目：给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值
"""
import heapq


def maxSlidingWindow_1(nums, k):
    length = len(nums)
    max_value = []
    for i in range(0, length - k + 1):
        window = nums[i:i + k]
        max_value.append(max(window))
    return max_value


def maxSlidingWindow_2(nums, k):
    length = len(nums)
    max_value = []
    for i in range(0, length - k + 1):
        window = nums[i:i + k]
        reverse_window = [-i for i in window]
        heapq.heapify(reverse_window)
        max_value.append(-reverse_window[0])
    return max_value


def maxSlidingWindow_3(nums, k):
    length = len(nums)
    window = [(-nums[i], i) for i in range(k)]
    heapq.heapify(window)

    max_value = [-window[0][0]]
    for i in range(k, length):
        heapq.heappush(window, (-nums[i], i))
        # 当前元素在滑动窗口左边界外，删除
        while window[0][1] <= i-k:
            heapq.heappop(window)
        max_value.append(-window[0][0])
    return max_value


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = maxSlidingWindow_3(nums, k)
    print(result)
