from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        思路：动态规划
        dp[i] 表示“考虑前 i 个房子（下标 0..i-1）时，能偷到的最大金额”
        转移：
          - 不偷第 i 个房子（下标 i-1）：dp[i] = dp[i-1]
          - 偷第 i 个房子：dp[i] = dp[i-2] + nums[i-1]
        所以：
          dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        """

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # 空间优化：只保留 dp[i-2] 和 dp[i-1]
        prev2 = 0          # dp[i-2]，初始化 dp[0] = 0
        prev1 = 0          # dp[i-1]，初始化 dp[1] 之后会更新

        for money in nums:
            # 当前 dp 值：要么不偷当前房子(prev1)，要么偷当前房子(prev2 + money)
            cur = max(prev1, prev2 + money)

            # 滚动更新：为下一轮做准备
            prev2 = prev1
            prev1 = cur

        return prev1
"""


时间复杂度：O(n)
空间复杂度：O(1)

"""