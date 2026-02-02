from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        单调递减栈：栈中存下标，使得 temperatures[栈底] >= ... >= temperatures[栈顶]
        遍历到更高温度时，依次结算那些更低温度的天数差。
        """
        n = len(temperatures)
        ans = [0] * n
        stack = []  # 存下标，维护单调递减温度

        for i, t in enumerate(temperatures):
            # 只要当前温度比栈顶那天温度高，就找到了栈顶那天的“下一个更高温度”
            while stack and t > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            # 当前天入栈，等待未来更高温度来结算
            stack.append(i)

        return ans



"""
Docstring for BasicDataStructure.Stack.dailyTemperature
算法思路（Monotonic Stack）
我们要对每一天 i 找到右边第一个温度更高的天 j，答案是 j - i，找不到则 0。
用一个栈存下标，并保持栈中对应温度单调递减（从栈底到栈顶温度越来越低/不升）：
遍历 i = 0..n-1：
    当 temperatures[i] > temperatures[stack[-1]] 时，说明 i 就是栈顶那一天的“下一次更高温度”，不断弹栈并填答案：
        prev = stack.pop()
        ans[prev] = i - prev
    最后把 i 入栈，等待将来被更高温度“结算”


时空复杂度
设 n = len(temperatures)：
    时间复杂度：O(n)
        每个下标最多入栈一次、出栈一次，总操作次数线性。
    空间复杂度：O(n)
        最坏情况下温度单调递减，所有下标都在栈里。




"""

