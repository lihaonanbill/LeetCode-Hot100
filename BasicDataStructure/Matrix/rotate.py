from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        将 n x n 矩阵顺时针旋转 90 度（原地修改，不返回）。
        思路：转置 + 每行反转
        """
        n = len(matrix)
        if n == 0:
            return

        # 1) 转置：matrix[i][j] <-> matrix[j][i]
        # 只交换上三角（不含对角线）即可，避免重复交换
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2) 每行反转：把转置后的矩阵左右翻转
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1




"""
算法思路（为什么“转置 + 反转行”= 顺时针 90°)
    设原矩阵元素在位置 (i,j)。
        顺时针旋转 90° 的目标位置是：
        (i,j)→(j,n-1-i)
    分两步看：
        转置：(i,j)→(j,i)
        每行反转（左右翻转）：行号不变，列 i→n-1-i
        所以 (j,i)→(j,n-1-i)
    两步合起来正好是顺时针 90°。

时空复杂度
    时间复杂度：
        转置交换约 n(n-1)/2 次
        反转每行约 n/2 次交换，共 n⋅(n/2)
        总体都是 O(n^2)
    空间复杂度：
        只用了几个临时变量交换,O(1) 额外空间（不算输入矩阵本身.


"""