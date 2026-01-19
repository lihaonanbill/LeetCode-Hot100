"""
Docstring for CoreAlgorithmicIdeasAndTechnique.DynamicProgramming.climbStairs





"""
class Solution:
    def climbStairs(self, n: int) -> int:
        # 特判：n = 1 时只有 1 种走法
        if n == 1:
            return 1

        # a = dp[i-2], b = dp[i-1]
        # 对应 dp[1]=1, dp[2]=2
        a, b = 1, 2

        # 从第 3 阶开始递推到第 n 阶
        for _ in range(3, n + 1):
            a, b = b, a + b  # 新的 dp[i] = dp[i-1] + dp[i-2]

        return b  # b 最终就是 dp[n]


"""


算法思路（DP / 斐波那契）

设 dp[i] 表示：爬到第 i 阶的方法数。

到第 i 阶，最后一步只能来自：
第 i-1 阶走 1 步
第 i-2 阶走 2 步
所以递推：
dp[i]=dp[i−1]+dp[i−2]

初始条件：
dp[1] = 1
dp[2] = 2
因为只依赖前两项，用两个变量滚动即可（O(1) 空间）。




我有个问题啊，所以动态规划的定义是什么呢？为什么说这个是动态规划？


"""