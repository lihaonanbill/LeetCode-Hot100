from typing import List

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res: List[str] = []
#         path: List[str] = []  # 用字符数组存路径，最后 join 成字符串

#         def dfs(open_cnt: int, close_cnt: int) -> None:
#             # 终止：长度达到 2n，说明用了 n 对括号
#             if open_cnt == n and close_cnt == n:
#                 res.append("".join(path))
#                 return

#             # 选择 1：还能放左括号
#             if open_cnt < n:
#                 path.append('(')
#                 dfs(open_cnt + 1, close_cnt)
#                 path.pop()

#             # 选择 2：只有当右括号数量 < 左括号数量时，才能放右括号（保证前缀合法）
#             if close_cnt < open_cnt:
#                 path.append(')')
#                 dfs(open_cnt, close_cnt + 1)
#                 path.pop()

#         dfs(0, 0)
#         return res





"""
Docstring for AdvancedDataStructureAndGraph.BackTracking.generateParenthesis

算法思路（回溯构造 + 合法性约束）
用两个计数：
    open_cnt：已放入的 '(' 数量
    close_cnt：已放入的 ')' 数量
递归构造字符串 path：
    如果 open_cnt < n：可以继续放 '('
    如果 close_cnt < open_cnt：可以放 ')'（保证任意前缀里 ) 不会多于 (）
    当 len(path) == 2*n：得到一个完整合法序列，加入答案


    
eg: n=3

"" (0,0)
└─ "(" (1,0)
   ├─ "((" (2,0)
   │  ├─ "(((" (3,0)
   │  │  └─ "((()" (3,1)
   │  │     └─ "((())" (3,2)
   │  │        └─ "((()))" (3,3)   ✅
   │  └─ "(()" (2,1)
   │     ├─ "(()(" (3,1)
   │     │  └─ "(()()" (3,2)
   │     │     └─ "(()())" (3,3)  ✅
   │     └─ "(())" (2,2)
   │        └─ "(())(" (3,2)
   │           └─ "(())()" (3,3)  ✅
   └─ "()" (1,1)
      └─ "()(" (2,1)
         ├─ "()((" (3,1)
         │  └─ "()(()" (3,2)
         │     └─ "()(())" (3,3)  ✅
         └─ "()()" (2,2)
            └─ "()()(" (3,2)
               └─ "()()()" (3,3)  ✅



什么是卡特兰数



"""

