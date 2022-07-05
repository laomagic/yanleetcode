# coding:utf-8
"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
1.每行中的整数从左到右按升序排列。
2.每行的第一个整数大于前一行的最后一个整数。

二位矩阵搜索某元素target
"""


def searchMatrix_1(matrix, target):
    if not matrix:
        return False
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            element = matrix[i][j]
            if element == target:
                return True
    return False


def searchMatrix_2(matrix, target):
    if not matrix:
        return False
    row = 0
    col = len(matrix[0]) - 1
    while row <= len(matrix) - 1 and col >= 0:
        element = matrix[row][col]
        if element == target:
            return True
        elif element < target:
            row += 1
        else:
            col -= 1
    return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 34
    result = searchMatrix_2(matrix, target)
    print(result)
