from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int) -> None:
            # 越界 或 不是陆地（已经是水/已访问）就返回
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return

            # 标记为已访问：把陆地淹掉
            grid[r][c] = '0'

            # 继续扩展四个方向
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)  # 把整个岛屿都标记掉

        return islands


"""
Docstring for AdvancedDataStructureAndGraph.GraphTheory.numIslands
算法思路（DFS 泛洪填充）
    扫描每个格子 (r, c)：
        如果是 '1'，说明发现了一个新岛屿，计数 ans += 1
        立刻从它出发做 DFS，把与它 上下左右连通 的所有 '1' 都改成 '0'（表示已访问）
    扫描结束后，ans 就是岛屿数量。
    “改成 0” 相当于 visited 标记，省空间。

复杂度
    时间复杂度：O(m*n)
        每个格子最多被访问/改写一次。
    空间复杂度：O(m*n)（最坏递归深度，整张图都是陆地时）
        实际上是递归栈空间；如果担心递归爆栈，可以用 BFS/栈迭代把空间控制在队列/栈上。

"""