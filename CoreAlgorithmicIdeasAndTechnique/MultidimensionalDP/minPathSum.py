from typing import List

# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         """
#         动态规划 + 滚动数组（空间优化）
        
#         dp[j] 表示当前处理到的行 i 中，到达列 j 的最小路径和。
#         更新前 dp[j] 是上一行 (i-1, j) 的最小路径和；
#         dp[j-1] 是当前行 (i, j-1) 的最小路径和（已经更新过）。
#         """
#         m, n = len(grid), len(grid[0])

#         # dp 初始化为第一行的最小路径和（只能一直往右走）
#         dp = [0] * n
#         dp[0] = grid[0][0]
#         for j in range(1, n):
#             dp[j] = dp[j - 1] + grid[0][j]

#         # 从第二行开始逐行更新 dp
#         for i in range(1, m):
#             # 第 i 行第 0 列只能从上方走下来
#             dp[0] = dp[0] + grid[i][0]
#             for j in range(1, n):
#                 # dp[j]：上方；dp[j-1]：左方
#                 dp[j] = grid[i][j] + min(dp[j], dp[j - 1])

#         return dp[-1]



"""
算法思路： 动态规划
    dp[i][j]=grid[i][j]+min(dp[i−1][j], dp[i][j−1])

空间优化：
    dp[i][j] 只依赖 dp[i-1][j]（上一行同列）和 dp[i][j-1]（当前行左边）。
    所以用一维数组 dp[j]：
        更新前 dp[j] 表示“上一行的 dp[i-1][j]”
        更新后 dp[j] 变成“当前行的 dp[i][j]”
    转移变为：
        dp[j]=grid[i][j]+min(dp[j], dp[j−1])

T: O(mn)
S: O(n)
"""

