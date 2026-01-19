from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1.用哈希集合查找 2.去重
        s = set(nums)
        best = 0

        for x in s:
            # 只从“序列起点”开始扩展，避免重复计算
            # 一个数x是某个连续序列的起点当且仅当x-1不在集合中
            if x - 1 not in s:
                cur = x
                length = 1
                # 从起点向右扩展，计算长度
                while cur + 1 in s:
                    cur += 1
                    length += 1
                best = max(best, length)

        return best
"""
题目要求：
    找 数值连续 的最长序列
    不要求在原数组中连续
    要求 O(n) 时间复杂度


思路：
    利用哈希集合O(1)查找，只从连续序列起点开始扩展，每个元素最多访问一次，因此时间复杂度O(n), 空间复杂度O(n)

s = set(nums)的作用：

    

"""