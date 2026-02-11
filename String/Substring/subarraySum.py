from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # cnt[p] 表示“前缀和等于 p”出现的次数
        cnt = defaultdict(int)
        cnt[0] = 1  # 空前缀：前缀和为 0 出现 1 次

        pre = 0      # 当前前缀和
        ans = 0      # 结果：和为 k 的子数组个数

        for x in nums:
            pre += x

            # 若存在某个历史前缀和 = pre - k
            # 则这些位置到当前的子数组和都为 k
            ans += cnt[pre - k]

            # 记录当前前缀和出现次数
            cnt[pre] += 1

        return ans



"""
Docstring for String.Substring.subarraySum

算法思路（前缀和 + 计数）
    设前缀和 pre[i] = nums[0] + ... + nums[i]。
    子数组 nums[l..i] 的和为：
        pre[i]−pre[l−1]
    要它等于 k，则需要：
        pre[l−1]=pre[i]−k
    所以我们遍历数组维护当前前缀和 pre，并用哈希表 cnt 记录“某个前缀和出现了多少次”。
    当遍历到当前位置前缀和为 pre 时：
        以当前位置结尾、和为 k 的子数组个数 = cnt[pre - k]
        然后把当前 pre 计数加 1
    初始化很关键：cnt[0] = 1，表示“空前缀和”为 0 出现一次，用来处理从下标 0 开始的子数组。

T: O(n)
S: O(n)

"""
