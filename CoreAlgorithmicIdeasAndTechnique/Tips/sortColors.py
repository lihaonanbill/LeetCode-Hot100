from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        荷兰国旗问题（三指针）
        原地排序，时间 O(n)，空间 O(1)
        """
        left = 0                  # 0 区域右边界
        right = len(nums) - 1     # 2 区域左边界
        i = 0                     # 当前遍历指针

        while i <= right:
            if nums[i] == 0:
                # 把 0 放到前面
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1

            elif nums[i] == 1:
                # 1 本来就在中间区域
                i += 1

            else:  # nums[i] == 2
                # 把 2 放到后面
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                # 注意这里 i 不增加
"""
核心思想：三指针

我们维护三个区域：

[0 ... left-1]     都是 0
[left ... i-1]     都是 1
[i ... right]      未处理
[right+1 ... end]  都是 2
"""