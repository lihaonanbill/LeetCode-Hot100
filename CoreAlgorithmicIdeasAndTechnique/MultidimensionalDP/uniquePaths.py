# 1. 动态规划（空间优化版）

# dp[i][j]=dp[i−1][j]+dp[i][j−1]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        动态规划（空间优化版）
        
        dp[j] 表示当前行第 j 列的路径数
        """
        
        # 初始化第一行，全部为1
        dp = [1] * n
        
        # 从第二行开始遍历
        for i in range(1, m):
            for j in range(1, n):
                # 当前格子 = 上方 + 左方
                # 上方是 dp[j]（上一轮的值）
                # 左方是 dp[j-1]
                dp[j] = dp[j] + dp[j-1]
        
        return dp[-1]




# 2.
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        数学组合解法
        """
        return math.comb(m + n - 2, m - 1)