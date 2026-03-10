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
如果：
    height[left] < height[right]
    那么当前位置 left 能接多少水，只由 leftMax 决定。
    因为此时右边一定存在一个至少和 height[right] 一样高的柱子，而 height[right] > height[left]，
    说明右侧挡板是够用的，真正限制当前位置装水高度的是左边最高值。
所以：
    若 height[left] < height[right]
        处理 left
    否则
        处理 right

可是如果height[left] < height[right]， 而right_max<left_max怎么办？

在双指针接雨水算法中，当 height[left] < height[right] 时，我们使用 left_max 来计算左边指针位置的水量。你担心如果此时 right_max < left_max，那么实际右边最高可能小于 left_max，导致计算偏大。但通过分析算法过程，可以证明这种情况实际上不会发生，或者即使发生，算法依然正确。

关键原因
    left_max 记录的是左边已遍历部分的最大值，而 right_max 记录的是右边已遍历部分的最大值。
    当进入左边分支（即 height[l] < height[r]）时，左边指针 l 正在移动。如果 left_max 大于右边整体的最大值（即 max(height[r], right_max)），那么左边指针应该停留在产生 left_max 的那个位置，因为只有右边出现更大的值才能让左边指针离开该位置。但此时右边整体最大值小于 left_max，所以左边指针不会移动，矛盾。
    因此，在左边分支中，必然有 left_max <= max(height[r], right_max)，即左边最高不超过右边实际最高，所以用 left_max 计算水量是正确的。
        
T: O(n)
S: 只用了场数个变量(l, r, left_max, right_max, water)
    O(1)

height = [0,1,0,2,1,0,1,3,2,1,2,1]

"""