from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        返回矩阵的螺旋（顺时针）遍历结果。
        """
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        res: List[int] = []

        # 四个边界：当前还没被遍历的“矩形区域”
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while top <= bottom and left <= right:
            # 1) 从左到右遍历 top 行
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1  # top 行已用完，向下收缩

            # 2) 从上到下遍历 right 列
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1  # right 列已用完，向左收缩

            # 注意：下面两步在“还剩有效区域”时才做
            # 3) 从右到左遍历 bottom 行
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1  # bottom 行已用完，向上收缩

            # 4) 从下到上遍历 left 列
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1  # left 列已用完，向右收缩

        return res



"""
Docstring for BasicDataStructure.Matrix.spiralOrder


算法思路
    把未遍历区域看成一个不断缩小的矩形，用四个指针表示边界：
        top：当前最上面那一行
        bottom：当前最下面那一行
        left：当前最左边那一列
        right：当前最右边那一列
    每一圈固定走 4 条边：
        top 行：左 → 右
        right 列：上 → 下
        bottom 行：右 → 左（前提 top <= bottom）
        left 列：下 → 上（前提 left <= right）
    走完一条边就把对应边界收缩，直到边界交错结束。
        两个 if 是为了避免剩下一行/一列时重复遍历（比如 1×n 或 m×1，或最后只剩一条边）。

时空复杂度
    时间复杂度：每个元素恰好加入一次 → O(m·n)
    额外空间复杂度：除了输出数组外只用常数变量 → O(1)（若算输出则为 O(m·n)）

我感觉这题需要注意的是while下面的两个if边界条件很容易被忽略
"""


