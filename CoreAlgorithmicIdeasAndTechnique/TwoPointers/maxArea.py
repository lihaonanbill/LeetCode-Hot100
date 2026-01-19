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

T: O(n)
S: O(1)



"""

if __name__ == "__main__":
    height = [1, 1]
    print(Solution().maxArea(height))