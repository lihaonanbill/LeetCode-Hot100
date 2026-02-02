from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        单调栈（递增栈）：
        栈中存下标，使得 heights[栈底] <= ... <= heights[栈顶]
        一旦遇到更矮的柱子，就可以确定被弹出柱子的“右边界”，并用当前下标确定宽度。
        """
        # 在末尾添加一个 0，保证最终能把栈清空结算
        h = heights + [0]

        stack = []  # 存下标
        max_area = 0

        for i, cur_height in enumerate(h):
            # 当前高度更小：说明栈顶柱子的“右边界”就是 i
            while stack and h[stack[-1]] > cur_height:
                mid = stack.pop()          # mid 是被结算的柱子下标（作为最矮高度）
                height = h[mid]

                # 弹出 mid 后，新的栈顶就是左边第一个更小柱子的下标
                left_smaller = stack[-1] if stack else -1
                # 右边第一个更小柱子是 i
                right_smaller = i

                width = right_smaller - left_smaller - 1
                max_area = max(max_area, height * width)

            # 当前柱子入栈
            stack.append(i)

        return max_area





"""
Docstring for BasicDataStructure.Stack.largestRectangleArea

算法思路（Monotonic Increasing Stack）
核心思想：对每根柱子 h[i]，如果把它作为“矩形的最矮高度”，它能向左右延伸到哪里？
    左边第一个 严格小于 h[i] 的位置记为 L
    右边第一个 严格小于 h[i] 的位置记为 R
    那么以 h[i] 为最矮高度的最大矩形宽度是 (R - L - 1)，面积是 h[i] * (R - L - 1)
用单调递增栈一次遍历就能在弹栈时确定 R，而弹出后的新栈顶就是 L。
实现技巧：
    在 heights 末尾加一个高度 0 的“哨兵”，强制把栈里所有柱子都弹出结算。
    栈里存的是下标，保持对应高度严格递增（或非递减也行，但需要统一处理，这里用 > 来触发弹栈，效果是维护非递减栈）。

时空复杂度
设 n = len(heights)：
    时间复杂度：O(n)
        每个下标最多入栈一次、出栈一次。
    空间复杂度：O(n)
        最坏情况下（单调递增高度）栈会存下所有下标。



Q: 这个算法是如何保证新的栈顶就是左边第一个更小柱子的下标
A: 因为当前高度只有不小于栈顶元素才能入栈
Q: h = heights + [0], 为什么可以把栈清空结算
A: 这个也许得归纳法证明一下，略
"""

