from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # 1) 收集所有初始腐烂橘子 + 统计新鲜橘子
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # 如果一开始就没有新鲜橘子
        if fresh == 0:
            return 0

        minutes = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 2) 多源 BFS：每一层代表 1 分钟
        while q:
            size = len(q)
            rotted_this_minute = False  # 这一分钟是否感染到新鲜橘子

            for _ in range(size):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    # 越界跳过
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # 只感染新鲜橘子
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
                        rotted_this_minute = True

            # 这一轮确实发生了感染，分钟数 +1
            if rotted_this_minute:
                minutes += 1

        # 3) 检查是否还有新鲜橘子
        return minutes if fresh == 0 else -1

"""
Docstring for AdvancedDataStructureAndGraph.GraphTheory.orangesRotting

算法思路（多源 BFS）
    扫描网格：
        把所有腐烂橘子（值为 2）的位置加入队列 queue
        统计新鲜橘子数量 fresh
    BFS 按“分钟”扩散：
        每一轮处理队列当前长度 size（这一轮代表同一分钟内会腐烂的传播源）
        对每个腐烂橘子，尝试感染上下左右的格子
        如果感染到新鲜橘子（1），改成 2，fresh -= 1，并入队
        如果这一轮至少感染了一个新鲜橘子，则 minutes += 1
    BFS 结束：
        若 fresh == 0，返回 minutes
        否则说明有新鲜橘子永远感染不到，返回 -1

复杂度
    时间复杂度：O(m*n)
        每个格子最多入队/出队一次。
    空间复杂度：O(m*n)（最坏情况下队列存很多格子）

所以size = len(q)表示上一分钟新增加的腐烂橘子数量
        
"""