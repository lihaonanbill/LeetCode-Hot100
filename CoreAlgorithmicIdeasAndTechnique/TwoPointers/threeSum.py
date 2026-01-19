from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 排序数组
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # 去重：固定第一个数时，跳过相同值
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 剪枝：排序后 nums[i] > 0，后面都 >= 0，不可能凑出 0
            if nums[i] > 0:
                break

            # 对固定的i，在区间[i+1, n-1]用双指针
            l, r = i + 1, n - 1
            while l < r:
                # 计算和
                s = nums[i] + nums[l] + nums[r]
                # 如果s=0
                if s == 0:
                    # 记录答案
                    res.append([nums[i], nums[l], nums[r]])
                    # 移动l,r
                    # 这里要同时移动吗？答：是的这样不会
                    l += 1
                    r -= 1
                    # l、r 去重：跳过重复值，避免重复三元组
                    # l<r这个条件是否必须加
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                # s<0, 说明和太小，l++
                elif s < 0:
                    l += 1
                # s>0, 说明和太大， r--
                else:
                    r -= 1

        return res

"""
T:
排序：O(n log n)
    外层枚举 i：O(n)
    内层双指针整体每轮 O(n)
    总计:
        （n^2 主导，排序项可忽略）

S: 
O(1)


因为是寻找不同数值对, i固定时, l,r要想不同必须同时变化，因此
    l += 1
    r -= 1


"""