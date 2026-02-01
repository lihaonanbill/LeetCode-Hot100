from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        原地将矩阵置零：如果 matrix[i][j] == 0，则将第 i 行和第 j 列全部置 0
        不返回，直接修改 matrix
        """
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])

        # 1) 先单独记录：第一行、第一列本身是否需要被置零
        first_row_has_zero: bool = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero: bool = any(matrix[i][0] == 0 for i in range(m))

        # 2) 用第一行、第一列作为“标记区”
        #    若 matrix[i][j] == 0 (i>0, j>0)，则标记：
        #    matrix[i][0] = 0 表示第 i 行要清零
        #    matrix[0][j] = 0 表示第 j 列要清零
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 3) 根据标记清零内部区域（不动第一行/第一列）
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 4) 最后处理第一行、第一列（因为它们被当作标记用过）
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0





"""
Docstring for BasicDataStructure.Matrix.setZeroes


算法思路（为什么这样做对）
    题目要求“看到 0 就把整行整列清零”，但不能边扫边清（会把新出现的 0 误当原始 0，导致扩散）。
    解决办法是两阶段：
        先扫描并记录哪些行/列需要清零（这里把记录存在第一行、第一列里）。
        再根据记录统一清零。
    因为第一行/第一列被占用做标记，所以要额外用两个布尔变量保存它们“原本是否含 0”。

时空复杂度
    时间复杂度：
        扫描一次做标记 + 扫描一次清零 + 处理首行首列，都是 O(mn)
    空间复杂度：
        只用了 first_row_has_zero、first_col_has_zero 两个变量，额外空间 O(1)
"""


