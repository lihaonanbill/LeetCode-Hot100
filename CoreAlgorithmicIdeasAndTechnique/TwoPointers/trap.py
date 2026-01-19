from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # 用两个指针l,r分别从左右向中间移动
        l, r = 0, len(height) - 1
        # 维护：[0..l]区间见过的最高柱子; [r..n-1]区间见过的最高柱子
        left_max, right_max = 0, 0
        water = 0

        while l < r:
            # 如果height[l] < height[r]，说明左边这一侧的水位上限由left_max决定
            # (右边至少有height[r]作为边界， 不会比它更差)，因此可以确定l位置能装多少水：
            if height[l] < height[r]:
                # 若height[l] >= left_max，更新left_max
                if height[l] >= left_max:
                    left_max = height[l]
                # 否则加水
                else:
                    water += left_max - height[l]
                l += 1
            # 否则对称处理右边
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                r -= 1

        return water
"""

T: O(n)
S: 只用了场数个变量(l, r, left_max, right_max, water)
    O(1)

"""