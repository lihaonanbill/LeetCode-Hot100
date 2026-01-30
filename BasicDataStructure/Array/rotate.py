from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        不返回任何值，要求原地修改 nums，使其向右轮转 k 位。
        """

        n = len(nums)
        if n <= 1:
            return

        # 关键：k 可能 >= n，轮转 n 的倍数等于没动
        k %= n
        if k == 0:
            return

        # 原地翻转 nums[l..r]
        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # 思路：右移 k 位 等价于：
        # 1) 翻转整个数组
        # 2) 翻转前 k 个
        # 3) 翻转后 n-k 个
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
