"""
Docstring for CoreAlgorithmicIdeasAndTechnique.DynamicProgramming.numSquares
个人想法：
    先把100

"""

from typing import List

class Solution:
    def numSquares(self, n: int) -> int:
        """
        dp[x] 表示“凑出和为 x 所需的最少完全平方数个数”
        目标：dp[n]
        """

        # 1) 预先生成所有不超过 n 的完全平方数：1,4,9,...
        squares = []
        k = 1
        while k * k <= n:
            squares.append(k * k)
            k += 1

        # 2) 初始化 dp
        # dp[0] = 0：凑出 0 不需要任何数
        # 其余先设为无穷大（一个足够大的数）
        INF = 10**9
        dp = [INF] * (n + 1)
        dp[0] = 0

        # 3) 完全背包：每个平方数可以用无限次
        # 对每个平方数 s，尝试更新所有 x >= s
        for s in squares:
            for x in range(s, n + 1):
                # 使用一个 s，相当于 dp[x - s] + 1
                dp[x] = min(dp[x], dp[x - s] + 1)

        return dp[n]





"""
转移方程：
    选择一个平方数s, dp[x]=min(dp[x], dp[x-s+1])

T:O(n*(n**1/2))
S:O(n)

完全背包问题




"""