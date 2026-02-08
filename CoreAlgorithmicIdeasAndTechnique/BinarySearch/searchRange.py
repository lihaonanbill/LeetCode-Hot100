from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 找到第一个 >= x 的下标
        def lower_bound(x: int) -> int:
            left, right = 0, len(nums)  # 注意右边界取 len(nums)（半开区间）
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= x:
                    right = mid
                else:
                    left = mid + 1
            return left

        # 找到第一个 > x 的下标
        def upper_bound(x: int) -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > x:
                    right = mid
                else:
                    left = mid + 1
            return left

        # 1) 左边界：第一个 >= target
        left = lower_bound(target)

        # 若越界或不是 target，说明 target 不存在
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        # 2) 右边界：第一个 > target 的位置 - 1
        right = upper_bound(target) - 1

        return [left, right]


"""
Docstring for CoreAlgorithmicIdeasAndTechnique.BinarySearch.searchRange

算法思路
因为 nums 是非递减排序：
    左边界：找到第一个 >= target 的位置（lower_bound）
    右边界：找到第一个 > target 的位置（upper_bound），再减 1 得到最后一个等于 target 的位置
最后检查一下：若左边界越界或 nums[left] != target，说明不存在，返回 [-1, -1]。



试着这样想，在一段相同数字的区间，l,r取其中任意两个下标(l<r),
    对于lower_bound来说，右边界会不断左移，直到变成左边界
    对于upper_bound来说，左边界会不断右移，直到变成右边界

"""