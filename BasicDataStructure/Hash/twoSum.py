from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 记录“某个数值->它出现过的下标”
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need],i]
            seen[x] = i
        return []
"""
输入：nums = [2,7,11,15], target = 9
输出：[0,1]

T: O(n)
S: O(n)

"""