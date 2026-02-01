from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        在行、列都递增的二维矩阵中查找 target。
        返回 True/False。
        """
        # 边界：空矩阵或空行
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        # 从右上角开始： (0, n-1)
        i, j = 0, n - 1

        # 当仍在矩阵范围内时不断缩小搜索空间
        while i < m and j >= 0:
            cur = matrix[i][j]
            if cur == target:
                return True
            elif cur > target:
                # 当前值太大：这一列从上到下递增，cur 已经比 target 大
                # 所以 target 不可能在这一列的当前位置及其下方 -> 排除整列 j
                j -= 1
            else:
                # 当前值太小：这一行从左到右递增，cur 比 target 小
                # 所以 target 不可能在这一行的当前位置及其左侧 -> 排除整行 i
                i += 1

        return False


"""
Docstring for BasicDataStructure.Matrix.searchMatrix

算法思路（楼梯搜索）
    矩阵满足：
        每行从左到右递增
        每列从上到下递增
    选择 右上角 作为起点的原因：
        往左走：数变小
        往下走：数变大
    因此比较 cur 与 target：
        cur > target：往左（j -= 1），排除一整列
        cur < target：往下（i += 1），排除一整行
        相等直接返回 True
    每一步都能缩小搜索范围，最多走 m+n 步。

时空复杂度
    时间复杂度：最多移动 m 次向下 + n 次向左 → O(m + n)
    空间复杂度：只用常数变量 → O(1)


"""



