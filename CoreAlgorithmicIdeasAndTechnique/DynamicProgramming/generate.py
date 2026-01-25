from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # res 用来存放最终的杨辉三角
        res: List[List[int]] = []

        # 逐行生成：第 i 行有 i+1 个元素（i 从 0 开始）
        for i in range(numRows):
            # 初始化当前行：全部先填 1（因为每行两端都是 1）
            row = [1] * (i + 1)

            # 计算中间位置的值：row[j] = 上一行的 j-1 和 j 之和
            # 只有当 i >= 2 时才存在“中间元素”
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]

            # 把当前行加入结果
            res.append(row)

        return res
"""


"""