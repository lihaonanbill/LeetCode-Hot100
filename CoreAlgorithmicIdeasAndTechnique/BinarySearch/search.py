from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # 命中直接返回
            if nums[mid] == target:
                return mid

            # 判断哪一半是有序的
            if nums[left] <= nums[mid]:
                # 左半边 [left, mid] 有序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # target 在左半边
                else:
                    left = mid + 1   # target 在右半边
            else:
                # 右半边 [mid, right] 有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # target 在右半边
                else:
                    right = mid - 1  # target 在左半边

        # 没找到
        return -1

"""
Docstring for CoreAlgorithmicIdeasAndTechnique.BinarySearch.search

算法思路
在旋转数组中，任意区间 [left, right] 内，mid 会把区间分成两半，其中 至少有一半是严格有序的：
    若 nums[left] <= nums[mid]：说明 左半边有序
        如果 target 在 [nums[left], nums[mid]) 之间 → 去左边
        否则 → 去右边
    否则：说明 右半边有序
        如果 target 在 (nums[mid], nums[right]] 之间 → 去右边
        否则 → 去左边
直到找到或区间为空。


能不能把
if nums[left] <= target < nums[mid]:改为
if target < nums[mid]:
不能，因为右边也有可能比nums[mid]小

"""


