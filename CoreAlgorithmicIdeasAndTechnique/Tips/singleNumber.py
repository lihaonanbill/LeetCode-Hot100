from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        使用异或：成对元素抵消，最终剩下的就是只出现一次的数。
        """
        ans = 0
        for x in nums:
            ans ^= x
        return ans
    
"""
算法思路（异或 XOR）
    题目条件：除了一个元素出现一次，其余元素都出现两次。
    利用异或性质：
        a ^ a = 0（相同抵消）
        a ^ 0 = a
        异或满足交换律、结合律：顺序无关
    把所有数字依次异或起来：
        成对出现的数字会全部抵消成 0
        最后剩下的就是那个只出现一次的数字

"""