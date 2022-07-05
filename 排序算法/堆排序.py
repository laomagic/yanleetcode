# coding:utf-8
"""
堆排序：
    堆排序是利用堆这种数据结构所设计的一种排序算法
    1.将待排序的数组初始化为大顶堆，该过程即建堆。
    2.将堆顶元素与最后一个元素进行交换，除去最后一个元素外可以组建为一个新的大顶堆。
    3.由于第二部堆顶元素跟最后一个元素交换后，新建立的堆不是大顶堆，需要重新建立大顶堆。重复上面的处理流程，直到堆中仅剩下一个元素。
"""


def build_heap(nums, i, l):
    # 叶子节点索引
    left = 2 * i + 1
    right = 2 * i + 2
    # 父节点索引
    parent_index = i
    if left < l and nums[parent_index] < nums[left]:
        parent_index = left
    if right < l and nums[right] > nums[parent_index]:
        parent_index = right

    # 非父节点的索引，元素交换，继续调整
    if parent_index != i:
        nums[i], nums[parent_index] = nums[parent_index], nums[i]
        # 继续调整
        build_heap(nums, parent_index, l)


if __name__ == '__main__':
    nums = [10, 50, 2, 4, 6, 1]
    # 遍历父节点初始化堆
    for i in range(len(nums) // 2 - 1, -1, -1):
        print(i)
        # 构建大顶堆
        build_heap(nums, i, len(nums))

    # 排序 交换堆顶和堆底元素
    for j in range(len(nums) - 1, -1, -1):
        nums[0], nums[j] = nums[j], nums[0]
        # 调整堆
        build_heap(nums, 0, j)
    print(nums)
