from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 当前以 nums[i] 结尾的最大子数组和（滚动 dp）
        cur = nums[0]
        # 全局最大子数组和
        best = nums[0]

        for i in range(1, len(nums)):
            # 要么把 nums[i] 接到前面的最优结尾子数组后面
            # 要么从 nums[i] 自己重新开始一个子数组
            cur = max(nums[i], cur + nums[i])
            # 更新全局最大值
            best = max(best, cur)

        return best
"""
时空复杂度

时间复杂度： O(n)（只遍历一次数组）

空间复杂度： O(1)（只用常数个变量）



"""