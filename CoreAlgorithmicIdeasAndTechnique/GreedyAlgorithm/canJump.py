from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0  # 当前能到达的最远下标

        for i in range(n):
            # 如果当前位置都到不了，说明出现断点，无法继续
            if i > farthest:
                return False

            # 用当前位置的跳跃能力更新最远可达位置
            farthest = max(farthest, i + nums[i])

            # 已经可以到达或超过最后一个下标
            if farthest >= n - 1:
                return True

        # return True  # 能遍历完说明都可达（包括 n=1 的情况）

"""
Docstring for CoreAlgorithmicIdeasAndTechnique.GreedyAlgorithm.canjump
算法思路（贪心）
从左到右遍历，维护目前最远能到达的位置 farthest。
    当前位置 i 如果已经 超过 farthest，说明连 i 都到不了，后面更不可能到 → 返回 False
    否则用 farthest = max(farthest, i + nums[i]) 更新最远可达
    一旦 farthest >= n-1，说明能到最后 → 返回 True


1. farthest >= n - 1就说明一定可以到达吗
2. 什么是能遍历完说明可达

"""
