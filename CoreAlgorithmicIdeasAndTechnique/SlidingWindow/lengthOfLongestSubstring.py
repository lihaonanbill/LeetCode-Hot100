class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # last[c] = 字符 c 最近一次出现的位置
        last = {}

        left = 0          # 当前窗口左边界
        best = 0          # 最长无重复子串长度

        for right, ch in enumerate(s):
            # 如果 ch 在 last 中，并且它的上次出现位置在窗口内 => 产生重复
            if ch in last and last[ch] >= left:
                # 把 left 移到重复字符上次出现位置的后一个位置
                left = last[ch] + 1

            # 更新 ch 的最新位置
            last[ch] = right

            # 更新答案
            best = max(best, right - left + 1)

        return best



"""
Docstring for CoreAlgorithmicIdeasAndTechnique.SlidingWindow.lengthOfLongestSubstring
算法思路（滑动窗口）

维护一个窗口 [left, right]，保证窗口内没有重复字符。
    用 last[c] 记录字符 c 最近一次出现的下标
    当扫描到 s[right]=c：
        如果 c 之前出现过，并且 last[c] >= left，说明它在当前窗口内重复了
        👉 需要把 left 移到 last[c] + 1，把重复的那次排除掉
        更新 last[c] = right
        用 right-left+1 更新答案
关键点：left = max(left, last[c] + 1)，防止 left 回退。

"""

