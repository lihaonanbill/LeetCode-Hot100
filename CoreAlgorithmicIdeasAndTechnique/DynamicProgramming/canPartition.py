from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # 总和为奇数，不可能平分
        if total % 2 == 1:
            return False

        target = total // 2

        # dp[j] 表示是否能用前面处理过的数字凑出和 j
        dp = [False] * (target + 1)
        dp[0] = True

        for x in nums:
            # 倒序更新，避免同一个数被重复使用
            for j in range(target, x - 1, -1):
                if dp[j - x]:
                    dp[j] = True

            # 提前结束：已经能凑出 target
            if dp[target]:
                return True

        return dp[target]
"""

算法思路（0/1 背包：子集和）
    1.计算总和 S = sum(nums)
        若 S 是奇数，必不可能分成两个相等子集，直接返回 False
    2.目标变为：是否存在子集和等于 target = S//2
    3.用一维 DP：
        dp[j] = True/False 表示“是否能选若干个数凑出和 j”
        初始化：dp[0] = True（不选任何数凑出 0）
        对每个数 x，倒序更新 j = target ... x：？
        dp[j] = dp[j] or dp[j-x]
        倒序是为了保证每个数只用一次（0/1 背包）


时空复杂度
    设 n = len(nums), target = sum(nums)/2
    时间复杂度：O(n * target)
    空间复杂度：O(target)

倒序：为了解决重复使用的问题

倒序更新确保了：当我们要用当前数字 x 来凑和 j 时，我们检查的是 不用当前数字 能否凑出 j-x 的状态 dp[j-x]。
如果我们正序更新，那么在处理当前数字 x 时，dp[j-x] 可能已经被更新过，表示“用当前数字 x 能否凑出 j-x”，这会导致同一个数字被重复使用。



归纳基础：
    初始时，dp[0] = True（空集合的和为0）
    这是正确的数学事实

归纳假设：
    假设在处理前 k 个数字后，对于任意和 s：
    dp[s] = True 当且仅当存在前 k 个数字的某个子集，其和为 s

归纳步骤：
    考虑第 k+1 个数字 x：
    不选 x：能凑出的和不变，即保持原来的 dp 值
    选 x：如果原来能凑出 j-x，现在就能凑出 j
    由于我们倒序更新，确保 dp[j-x] 是考虑前 k 个数字时的状态，不会包含当前数字 x，所以不会重复使用
"""