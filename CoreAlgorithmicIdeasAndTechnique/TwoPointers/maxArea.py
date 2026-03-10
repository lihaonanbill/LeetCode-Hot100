from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 初始化两端指针
        l, r = 0, len(height) - 1
        # 记录最大面积
        best = 0

        while l < r:
            h = min(height[l], height[r])
            best = max(best, h * (r - l))

            # 移动较短的那一侧，才可能提高 min(height[l], height[r])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return best
    



"""
盛最多水的容器

为什么要移动较短的那一边？

当前面积由两部分决定：
    宽度：right - left
    高度：min(height[left], height[right])
此时如果移动较高的一边：
    宽度一定变小
    高度上限仍然受较短边限制
    面积不可能变得更优
所以应该移动 较短的那一边，因为：
    虽然宽度变小了
    但较短边有机会变高
    才可能得到更大的面积
这就是双指针贪心的核心。

T: O(n)
S: O(1)



"""

if __name__ == "__main__":
    height = [1, 1]
    print(Solution().maxArea(height))