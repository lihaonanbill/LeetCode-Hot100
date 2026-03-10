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

排序 + 双指针

这题的经典做法是：

第一步：先排序
    将数组从小到大排序。
    例如：
        [-1, 0, 1, 2, -1, -4]
    排序后变成：
        [-4, -1, -1, 0, 1, 2]
    排序的作用有两个：
        方便使用双指针
        方便去重
第二步：固定第一个数，转化为两数之和
    我们枚举第一个数 nums[i]，然后在区间 [i+1, n-1] 中找两个数，使得：
        nums[left]+nums[right]=−nums[i]
    这就变成了经典的“两数之和（有序数组版）”。
第三步：双指针查找
对于固定的 i：
    left = i + 1
    right = n - 1
然后计算：
    um=nums[i]+nums[left]+nums[right]
    如果 sum == 0，找到一个答案
    如果 sum < 0，说明和太小，需要让它变大，left++
    如果 sum > 0，说明和太大，需要让它变小，right--


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