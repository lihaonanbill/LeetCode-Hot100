from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # cur_max: 以当前元素结尾的子数组最大乘积
        # cur_min: 以当前元素结尾的子数组最小乘积（为了处理负数翻转）
        cur_max = cur_min = nums[0]
        ans = nums[0]

        for x in nums[1:]:
            # 因为更新 cur_max 会用到旧的 cur_max，所以先存起来
            prev_max, prev_min = cur_max, cur_min

            # 当前位置结尾的最大/最小乘积，来自三种选择：
            # 1) 从当前 x 重新开始
            # 2) 接在之前最大乘积后面
            # 3) 接在之前最小乘积后面（乘负数可能变大）
            cur_max = max(x, prev_max * x, prev_min * x)
            cur_min = min(x, prev_max * x, prev_min * x)

            ans = max(ans, cur_max)

        return ans
"""

算法思路（动态规划 / 状态压缩）

    设：
        cur_max[i] = 以 i 结尾的子数组最大乘积
        cur_min[i] = 以 i 结尾的子数组最小乘积

    转移：  
        cur_max[i] = max(nums[i], cur_max[i-1]*nums[i], cur_min[i-1]*nums[i])
        cur_min[i] = min(nums[i], cur_max[i-1]*nums[i], cur_min[i-1]*nums[i])

    由于只依赖 i-1，用两个变量滚动即可
T: O(n)
S: O(1)


"""