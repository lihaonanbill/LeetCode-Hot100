from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        返回所有分割方案，使得每个子串都是回文串。
        """
        n = len(s)
        res: List[List[str]] = []
        path: List[str] = []

        # 1) 预处理：pal[i][j] 表示 s[i..j] 是否为回文（闭区间）
        pal = [[False] * n for _ in range(n)]
        # 按长度从小到大填表，保证用到 pal[i+1][j-1] 时已计算
        for length in range(1, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    # 长度 1 或 2：只要两端相等就是回文
                    if length <= 2:
                        pal[i][j] = True
                    else:
                        # 长度 >= 3：看中间 s[i+1..j-1] 是否回文
                        pal[i][j] = pal[i + 1][j - 1]

        # 2) 回溯：从 start 开始切分
        def backtrack(start: int) -> None:
            # 切到字符串末尾，收集一种方案
            if start == n:
                res.append(path.copy())
                return

            # 枚举下一段子串 s[start:end+1]
            for end in range(start, n):
                if not pal[start][end]:
                    continue

                # 选择：加入当前回文段
                path.append(s[start:end + 1])

                # 递归：从 end+1 继续切
                backtrack(end + 1)

                # 撤销选择
                path.pop()

        backtrack(0)
        return res

"""
算法思路
    这题的核心是：切分位置有很多种，用回溯枚举；但每次都用双指针去判断回文会重复计算很多次，所以先做 DP。
    1）DP 预处理回文
    定义：
        pal[i][j] = True 表示 s[i..j] 是回文（闭区间）
    递推：
        若 s[i] != s[j]：一定不是回文
        若 s[i] == s[j]：
            长度 <= 2（如 "a" 或 "aa"）一定是回文
            否则看中间 pal[i+1][j-1]
    这样填完表后，回溯时判断某段是否回文只要 O(1) 查表。
    2）回溯枚举切分
    从位置 start 出发，枚举所有可能的 end：
        如果 s[start..end] 是回文，就把它放进 path，递归处理 end+1
        当 start == n，说明切到了末尾，path 就是一种合法方案

时空复杂度
    设 n = len(s)。
    DP 预处理：二维表 n*n，每格 O(1) 计算
        时间：O(n²)
        空间：O(n²)
    回溯枚举：输出本身可能很多（最坏类似 s = "aaaa...."，切不切都行）
        方案数最坏是 2^(n-1) 级别
        每个方案复制/构造的总字符量平均在 O(n) 量级
        所以总体可写为：O(n² + n · 2^(n-1))（更常见写法：O(n² + n·2^n)）

下面的第二层循环时为了让j不溢出
for length in range(1, n + 1):
            for i in range(0, n - length + 1):
        
以 s = “aab” 为例：


为什么回溯枚举时间复杂度是O(n · 2^(n-1))?

预处理后，pal 表会标记出所有回文子串，如 “a”, “aa”, “b” 等。
回溯过程：
    起点 0，先选 “a”（回文），递归处理剩余 “ab”。
        在 “ab” 中，起点 1，选 “a”（回文），递归处理剩余 “b”。
            在 “b” 中，起点 2，选 “b”（回文），到达末尾，记录方案 [“a”, “a”, “b”]。
        回溯，在 “ab” 中起点 1 尝试 “ab”，不是回文，跳过。
    回溯到起点 0，尝试 “aa”（回文），递归处理剩余 “b”。
        在 “b” 中，起点 2，选 “b”（回文），记录方案 [“aa”, “b”]。
    继续尝试 “aab”，不是回文，跳过。
    最终得到两种分割方案：[[“a”, “a”, “b”], [“aa”, “b”]]。
"""