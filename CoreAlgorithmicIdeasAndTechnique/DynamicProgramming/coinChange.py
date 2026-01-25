from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp[x] 表示“凑出金额 x 所需的最少硬币数”
        目标：dp[amount]
        若无法凑出，返回 -1
        """

        # 特判：金额为 0，不需要硬币
        if amount == 0:
            return 0

        # 用一个足够大的数表示“不可达/无穷大”
        INF = amount + 1  # 最坏情况用 amount 个 1 元硬币（如果存在），所以 amount+1 一定够大
        dp = [INF] * (amount + 1)
        dp[0] = 0

        # 完全背包：每种硬币可无限次使用
        # 外层枚举硬币，内层金额从 coin 到 amount 递增
        for coin in coins:
            for x in range(coin, amount + 1):
                # 如果用一枚 coin，那么需要先凑出 x-coin，再加 1 枚
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != INF else -1
"""
设硬币种类数为 m = len(coins)：

时间复杂度：O(m⋅amount)

空间复杂度：O(amount)


"""