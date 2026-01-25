from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[i]：长度为 i+1 的递增子序列的“最小可能结尾值”
        tails = []

        for x in nums:
            # 找到 tails 中第一个 >= x 的位置
            i = bisect.bisect_left(tails, x)

            if i == len(tails):
                # x 比所有结尾都大，可以把某个递增子序列长度 +1
                tails.append(x)
            else:
                # 用更小的结尾值替换，保持长度不变但提升未来扩展性
                tails[i] = x

        return len(tails)
"""
greedy+binary search

i = bisect.bisect_left(tails, x)

这样的做法一定能保证找到最长递增子序列的长度吗？

deepseek的证明(又是归纳法doge)
https://chat.deepseek.com/share/q8amr9bd96vrvd9120

"""