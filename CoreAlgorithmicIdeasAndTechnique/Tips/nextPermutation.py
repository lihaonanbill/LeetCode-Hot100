from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        原地修改 nums 为字典序的下一个排列。
        若不存在更大的排列，则变为最小排列（升序）。
        """
        n = len(nums)
        if n <= 1:
            return

        # 1) 找到最右侧的 i，使得 nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 如果找不到 i，说明整体非递增：已是最大排列，反转为最小排列
        if i < 0:
            nums.reverse()
            return

        # 2) 从右往左找 j，使得 nums[j] > nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1

        # 3) 交换 i 和 j
        nums[i], nums[j] = nums[j], nums[i]

        # 4) 反转 i+1 到末尾，让后缀变成最小（升序）
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
"""
算法思路（字典序下一个排列）

要找“刚好比当前排列大一点点”的排列。

关键观察

从右往左看，后缀往往是非递增（例如 ... 5 4 3 2 1），这样的后缀已经是该后缀能形成的最大排列，想变大就必须改动它左边的某个位置。

步骤（必背模板）

    1.从右往左找第一个上升位置 i
        找到最右侧满足：nums[i]<nums[i+1]
        如果找不到，说明整个数组非递增（已经是最大排列），直接反转成最小排列并结束。
    2.从右往左找第一个比 nums[i] 大的元素 j
        在后缀里找最右侧满足：nums[j]>nums[i]
    3.交换 nums[i] 和 nums[j]
    4.反转 i+1 到末尾的后缀
        因为交换后，为了得到“最小的更大排列”，后缀需要变成最小（升序）。原后缀是非递增，反转即可得到升序。

"""