from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        返回 answer，其中 answer[i] = nums 中除 nums[i] 外所有元素的乘积
        要求：O(n) 时间，不使用除法
        进阶：O(1) 额外空间（输出数组 answer 不计入额外空间）
        """
        n = len(nums)
        answer = [1] * n

        # 1) 先计算每个位置 i 左边所有元素的乘积（前缀积）
        # answer[i] 最终会乘上 “左边乘积 * 右边乘积”
        # 这一步结束后：answer[i] = nums[0] * ... * nums[i-1]
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # 2) 再从右往左计算右边所有元素的乘积（后缀积），并直接乘到 answer[i] 上
        # suffix 表示 nums[i+1] * ... * nums[n-1]
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
"""
T: O(n)
S: O(1)
for i in range(n - 1, -1, -1)



"""