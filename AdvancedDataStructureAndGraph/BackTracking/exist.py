from typing import List
from collections import Counter

# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         """
#         回溯 + DFS
#         在 board 中寻找一条不重复使用格子的路径，使得路径字符按顺序拼出 word。
#         """
#         if not board or not board[0] or not word:
#             return False

#         m, n = len(board), len(board[0])
#         L = len(word)

#         # ---------- 剪枝 1：字符计数剪枝 ----------
#         board_cnt = Counter(ch for row in board for ch in row)
#         word_cnt = Counter(word)
#         for ch, need in word_cnt.items():
#             if board_cnt.get(ch, 0) < need:
#                 return False

#         # ---------- 剪枝 2：从更稀有的一端开始 ----------
#         # 如果 word[0] 比 word[-1] 更常见，就反转 word，从稀有字符开始搜
#         if board_cnt[word[0]] > board_cnt[word[-1]]:
#             word = word[::-1]

#         # 4 个方向：上、下、左、右
#         DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#         def dfs(r: int, c: int, i: int) -> bool:
#             """
#             尝试从 (r, c) 出发匹配 word[i:].
#             返回是否能成功匹配到末尾。
#             """
#             # 当前字符不匹配，直接失败
#             if board[r][c] != word[i]:
#                 return False

#             # 匹配到最后一个字符则成功
#             if i == L - 1:
#                 return True

#             # 标记当前格子已使用（避免重复使用）
#             tmp = board[r][c]
#             board[r][c] = '#'

#             # 尝试 4 个方向
#             for dr, dc in DIRS:
#                 nr, nc = r + dr, c + dc
#                 # 边界检查 + 未被访问（'#' 表示访问过）
#                 if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
#                     if dfs(nr, nc, i + 1):
#                         # 恢复现场再返回
#                         board[r][c] = tmp
#                         return True

#             # 回溯：恢复现场
#             board[r][c] = tmp
#             return False

#         # 枚举每个格子作为起点
#         for r in range(m):
#             for c in range(n):
#                 # 只有首字符匹配才值得 DFS（小剪枝）
#                 if board[r][c] == word[0] and dfs(r, c, 0):
#                     return True

#         return False





"""
Docstring for AdvancedDataStructureAndGraph.BackTracking.exist

算法思路（Backtracking / DFS）
我们要判断是否存在一条路径，按顺序拼出 word：
    可以从任意格子作为起点；
    每一步只能走到 上下左右 相邻格；
    同一个格子在一条路径中 不能重复使用。
做法：对每个格子 (r, c) 作为起点尝试 DFS：
    若当前格字符 != word[i]，失败
    否则标记该格已使用（常用做法：临时把 board[r][c] 改成一个特殊字符，比如 '#'）
    递归尝试匹配 word[i+1] 的四个方向
    递归结束后恢复现场（把字符改回去），继续其他分支
常见剪枝优化
    全局字符计数剪枝：如果 word 中某个字符出现次数 > board 中出现次数，直接返回 False。
    从更稀有的端开始：如果 word[0] 在 board 中比 word[-1] 更常见，可以把 word 反转，从更稀有字符开搜，通常更快。

    
复杂度分析
设网格大小为 m × n，单词长度为 L。
时间复杂度（最坏）：
    从每个格子出发，第一步最多 4 种选择，之后每步最多 3 种选择（不能回到刚来的格子），
    因此近似为：O(mn*4*3^(L-1))=O(mn*3^(L))
    实际会因剪枝与字符分布显著变快。
空间复杂度：
    使用原地标记，不额外开 visited 数组，主要是递归栈深度：O(L)


Counter()的返回结果是什么
for ch, need in word_cnt.items():
            if board_cnt.get(ch, 0) < need:
"""


