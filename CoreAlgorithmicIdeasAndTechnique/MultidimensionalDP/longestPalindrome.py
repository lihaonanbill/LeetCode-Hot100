class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        中心扩展法：
        枚举每个中心（i,i）和（i,i+1），向两侧扩展得到最长回文。
        """
        n = len(s)
        if n <= 1:
            return s

        # 记录当前找到的最长回文区间 [best_l, best_r]（闭区间）
        best_l, best_r = 0, 0

        def expand(l: int, r: int) -> tuple[int, int]:
            """
            从中心(l,r)开始向两侧扩展，返回最大回文的左右边界（闭区间）。
            """
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            # while 结束时 s[l]!=s[r] 或越界，回文实际是 (l+1, r-1)
            return l + 1, r - 1

        for i in range(n):
            # 1) 奇数回文：中心在 i
            l1, r1 = expand(i, i)
            if r1 - l1 > best_r - best_l:
                best_l, best_r = l1, r1

            # 2) 偶数回文：中心在 i 和 i+1 之间
            l2, r2 = expand(i, i + 1)
            if r2 - l2 > best_r - best_l:
                best_l, best_r = l2, r2

        return s[best_l:best_r + 1]

"""
算法思路：中心扩展（最常用、好写）
    回文串的“对称中心”有两种：
        奇数长度回文：中心是一个字符（如 "aba" 的 b）
        偶数长度回文：中心是两个字符之间（如 "abba" 的中间）
    做法：枚举每个可能中心，然后向两侧扩展，找到以该中心为轴的最长回文，取全局最长即可

T: O(n^2)
    一共有 2n 个中心
    每次扩展最坏 O(n)
S; O(1)

Q: 为什么时间复杂度是O(n^2)
"""