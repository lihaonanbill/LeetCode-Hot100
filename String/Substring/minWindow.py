from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        # need[c] 表示当前窗口还需要多少个字符 c 才能覆盖 t
        need = Counter(t)

        # missing 表示还缺多少“种”字符满足（当某字符需求降到 0，missing 才减 1）
        missing = len(need)

        left = 0
        best_len = float("inf")
        best_l = 0  # 记录最优窗口起点

        for right, ch in enumerate(s):
            # 扩张右端：如果 ch 在 need 中，说明它是 t 关心的字符
            if ch in need:
                need[ch] -= 1
                # 当 need[ch] 恰好变成 0，说明 ch 这种字符已经满足了
                if need[ch] == 0:
                    missing -= 1

            # 当 missing == 0，当前窗口 [left, right] 已覆盖 t
            while missing == 0:
                # 更新答案
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_l = left

                # 尝试收缩左端
                left_ch = s[left]
                if left_ch in need:
                    need[left_ch] += 1
                    # 如果 need[left_ch] 变成 1，说明丢掉这个字符后，窗口缺了它
                    if need[left_ch] == 1:
                        missing += 1  # 窗口不再合法，停止收缩
                left += 1

        return "" if best_len == float("inf") else s[best_l:best_l + best_len]


"""
Docstring for String.Substring.minWindow

算法思路（滑动窗口）
    目标：找到 s 中最短的子串 s[l..r]，使得它包含 t 中所有字符（包括重复次数）。
    关键思想
        用 need 记录 t 中每个字符需要的次数。
        用滑动窗口 [l, r] 在 s 上扩张右端 r：
            每加入一个字符 c = s[r]，如果它是需要的字符，就把需求次数减 1。
            当某个字符的需求从 1 变成 0，说明这个字符“满足了”。
        用 missing 表示“还缺多少种字符”（按字符种类，不按总个数）：
            当 missing == 0 时，窗口已经覆盖 t，尝试收缩左端 l，让窗口更短：
                如果 s[l] 是多余的（need[s[l]] < 0），就可以丢掉它并把需求加回去（从 -1 到 0）。
                一旦丢掉会导致缺字符（need[s[l]] == 0 时再丢），窗口就不再合法，停止收缩并继续扩张 r。
        在所有合法窗口中更新最短答案。

        

Q:
1.need中的元素可以变成负数  是的
2.need = Counter(t)的原理是什么 
3.s[best_l:best_l + best_len]这个是左闭右开吗  是的
"""

