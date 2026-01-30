from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        找出数组中缺失的最小正整数。
        要求：O(n) 时间，O(1) 额外空间（原地修改 nums）。
        """

        n = len(nums)

        # 核心思想：
        # 如果 1..n 这些数都在数组里，那么答案是 n+1
        # 所以我们只关心 [1, n] 范围内的数
        #
        # 目标：把每个值 x 放到下标 x-1 的位置上
        # 例如：值 1 应放到 index 0；值 2 应放到 index 1；...；值 n 放到 index n-1

        for i in range(n):
            # 当 nums[i] 是有效的正整数且应该放到正确位置时，就不断交换
            # 用 while 是因为交换后 nums[i] 变了，可能还需要继续放
            while 1 <= nums[i] <= n:
                correct_idx = nums[i] - 1  # nums[i] 应该去的位置
                if nums[correct_idx] == nums[i]:
                    # 说明目标位置已经是同样的值（重复元素），避免死循环
                    break
                # 把 nums[i] 放到它应该去的位置
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # 经过上面的“归位”后：
        # 如果 1 在数组中，那么 nums[0] 应该是 1
        # 如果 2 在数组中，那么 nums[1] 应该是 2
        # ...
        # 第一个不满足 nums[i] == i+1 的位置 i，说明 i+1 缺失
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 如果 1..n 都齐了，那么缺失的是 n+1
        return n + 1
"""
算法思路（为什么只看 1..n）
长度为 n 的数组里：
    如果 1..n 都出现了，那么最小缺失正数只能是 n+1
    如果缺失发生在更小的正整数里，它一定在 [1, n] 之间
所以我们只需把 [1, n] 范围内的数“放回自己应该在的位置”。



T: O(n)
S: O(1)

总结：
    这道题不是在找“缺什么”，
    而是在做一件事：
    把能用的正整数放回它该在的位置上。
    最后谁的位置不对，谁就是答案。

"""