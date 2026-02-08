from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)  # 搜索区间为 [l, r)

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < target:
                # 插入点一定在 mid 右侧
                l = mid + 1
            else:
                # nums[mid] >= target，插入点在左侧（包含 mid）
                r = mid

        # l == r，即第一个 >= target 的位置
        return l

# 左闭右闭
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # 搜索区间为 [l, r]（左闭右闭）

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                # 插入点一定在 mid 右侧
                l = mid + 1
            else:
                # nums[mid] >= target，插入点在左侧（包含 mid）
                r = mid - 1

        # 循环结束时：r < l
        # l 恰好指向第一个 >= target 的位置（也就是插入位置）
        return l
"""
Docstring for CoreAlgorithmicIdeasAndTechnique.BinarySearch.searchInsert

算法思路（lower_bound）
维护闭区间/半开区间都可以，我这里用更不容易出错的半开区间 [l, r)：
    初始：l = 0, r = len(nums)
    循环条件：l < r
    取中点：mid = (l + r) // 2
    若 nums[mid] < target：说明插入位置在右边，l = mid + 1
    否则（nums[mid] >= target）：插入位置在左边（包括 mid），r = mid
    循环结束时 l == r，即为插入位置

注意边界[l,r)
    
左闭右开：维护“答案在 [l,r) 里”，当 >=target 时保留 mid（所以 r=mid）

左闭右闭：维护“答案在 [l,r] 里”，当 >=target 时也要保留 mid，
但保留的方式是把 mid 放到右侧“已确认区”里，所以写成 r=mid-1，最终 l 会落到第一个满足的位置
"""