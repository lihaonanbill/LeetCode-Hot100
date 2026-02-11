from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        
        m, n = len(s), len(p)
        if n > m:
            return res
        
        # 统计 p 中字符频率
        need = [0] * 26
        for ch in p:
            need[ord(ch) - ord('a')] += 1
        
        # 滑动窗口统计
        window = [0] * 26
        
        left = 0
        
        for right in range(m):
            # 1. 扩张窗口（加入右端字符）
            idx = ord(s[right]) - ord('a')
            window[idx] += 1
            
            # 2. 当窗口长度超过 n，移除左端字符
            if right - left + 1 > n:
                left_idx = ord(s[left]) - ord('a')
                window[left_idx] -= 1
                left += 1
            
            # 3. 如果窗口大小刚好是 n，检查是否匹配
            if right - left + 1 == n:
                if window == need:
                    res.append(left)
        
        return res


"""
一、算法思路

目标：在 s 中找到所有长度为 len(p) 的子串，使其字符频率与 p 相同。
核心思想：
    维护两个长度为 26 的数组：
        need：记录 p 中每个字符出现次数
        window：记录当前窗口中字符出现次数
    用滑动窗口大小固定为 len(p)
    每次窗口右移：
        加入一个新字符
        如果窗口长度超过 len(p)，移除左端字符
        如果 window == need，说明找到一个异位词
"""