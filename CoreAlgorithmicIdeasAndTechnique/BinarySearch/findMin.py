from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # 当 left == right 时，区间收缩为一个元素，该元素即最小值
        while left < right:
            mid = (left + right) // 2

            # 如果 nums[mid] > nums[right]，说明最小值一定在 mid 的右边
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # nums[mid] < nums[right]（题目保证无重复），最小值在 [left, mid]
                right = mid

        return nums[left]


"""
Docstring for CoreAlgorithmicIdeasAndTechnique.BinarySearch.findMin

算法思路
旋转后的数组可以看成“两段有序递增”的拼接，最小值在“断点”处。
用二分维护区间 [left, right]，关键比较 nums[mid] 和 nums[right]：
    若 nums[mid] > nums[right]：说明 最小值在右半边（断点在 mid 右侧）
    → left = mid + 1
    否则（nums[mid] < nums[right]）：说明 最小值在左半边或就是 mid
    → right = mid
循环直到 left == right，该位置就是最小值。
"""
