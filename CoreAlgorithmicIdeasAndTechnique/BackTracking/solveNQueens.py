from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        返回所有 N 皇后解法，每个解法是一个字符串数组：
        'Q' 表示皇后，'.' 表示空位。
        """
        res: List[List[str]] = []

        # cols[c]：第 c 列是否已有皇后
        cols = [False] * n

        # 主对角线：row - col 取值范围 [-(n-1), (n-1)]
        # 用偏移 (n-1) 映射到 [0, 2n-2]
        diag1 = [False] * (2 * n - 1)  # (row - col + n - 1)

        # 副对角线：row + col 取值范围 [0, 2n-2]
        diag2 = [False] * (2 * n - 1)  # (row + col)

        # 用一个数组记录每一行皇后放在哪一列：pos[row] = col
        pos = [-1] * n

        def build_board() -> List[str]:
            """根据 pos 构造一个棋盘字符串表示"""
            board = []
            for r in range(n):
                row = ['.'] * n
                row[pos[r]] = 'Q'
                board.append(''.join(row))
            return board

        def backtrack(row: int) -> None:
            """
            尝试在第 row 行放皇后。
            每行只放一个皇后，因此天然不会有“同行冲突”。
            """
            if row == n:
                res.append(build_board())
                return

            for c in range(n):
                d1 = row - c + (n - 1)  # 主对角线索引
                d2 = row + c            # 副对角线索引

                # 若列/对角线被占用，则当前位置不可放
                if cols[c] or diag1[d1] or diag2[d2]:
                    continue

                # 选择：在 (row, c) 放皇后，并标记占用
                pos[row] = c
                cols[c] = True
                diag1[d1] = True
                diag2[d2] = True

                # 递归放下一行
                backtrack(row + 1)

                # 撤销选择（回溯）
                cols[c] = False
                diag1[d1] = False
                diag2[d2] = False
                pos[row] = -1

        backtrack(0)
        return res


"""
Docstring for AdvancedDataStructureAndGraph.BackTracking.solveNQueens
算法思路
    按行放置：第 row 行放一个皇后，所以不会出现同行冲突。
    对于 (row, col) 是否安全，只需检查三类冲突：
        同列：col 是否已被占用
        主对角线（\）：row - col 是否已被占用
        副对角线（/）：row + col 是否已被占用
    用 3 个布尔数组 cols/diag1/diag2 记录占用情况，这样冲突判断是 O(1)。
    每次放置后递归下一行；回溯时撤销标记。
    对角线索引为什么这样映射？
        主对角线：同一条对角线满足 row - col 相同，范围 [-(n-1), (n-1)]
        通过 + (n-1) 变成 [0, 2n-2]
        副对角线：同一条对角线满足 row + col 相同，范围 [0, 2n-2]

时空复杂度
时间复杂度：回溯搜索，最坏近似O(n!) 级别（实际因为剪枝远小于全排列，但量级仍指数/阶乘级）。
额外空间复杂度（不算输出答案）：
    pos、cols、diag1、diag2 都是 O(n) 或 O(2n)
    递归深度 O(n)
    总体 O(n)。


''.join()? 
board.append(''.join(row)) 
"""
