# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         # 栈里存“下标”，并用哨兵 -1 作为初始断点
#         stack = [-1]
#         ans = 0

#         for i, ch in enumerate(s):
#             if ch == '(':
#                 # '(' 记录位置，等待后面的 ')' 来匹配
#                 stack.append(i)
#             else:
#                 # ch == ')'
#                 # 尝试匹配：弹出一个位置（理想情况是与某个 '(' 匹配）
#                 stack.pop()

#                 if not stack:
#                     # 栈空了：说明当前 ')' 没法匹配
#                     # 把它当成新的断点位置
#                     stack.append(i)
#                 else:
#                     # 栈不空：说明形成了有效括号串
#                     # 以 i 结尾的最长有效长度 = i - 上一个断点位置
#                     # stack[-1]表示数组列表中最后一个元素
#                     ans = max(ans, i - stack[-1])

#         return ans

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        ans=0
        for i,ch in enumerate(s):
            if ch=='(':
                print(ch)
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans=max(ans,i-stack[-1])
                    print(ans)

if __name__ == "__main__":
    solution = Solution()
    s = "(()())"
    print(solution.longestValidParentheses(s))  # 输出: 6

"""
算法思路（栈存下标 + 哨兵）
    核心想法：
        遇到 '('：把它的下标入栈（等待匹配）
        遇到 ')'：尝试匹配一个 '('
            先弹栈（把一个待匹配位置拿出来）
            如果弹完栈空了：说明这个 ')' 没法匹配，它会成为新的“断点”，把它的下标压入栈当作新的基准
            如果弹完栈不空：说明匹配成功，此时以当前 i 结尾的最长有效长度是 i - stack[-1]
                stack[-1] 表示“上一个没法参与匹配的位置”（断点或更早的未匹配 '(' 的位置）
    为什么要放哨兵 -1：
        方便从开头就能计算长度，比如 "()" 在 i=1 时长度 = 1 - (-1) = 2

关键性质
1.栈底始终是"最后一个无效位置"
    开始时是 -1
    遇到无法匹配的 ')' 时更新
2.栈中 '(' 的位置都是未匹配的
    一旦被匹配，就会被弹出  
3.有效子串一定在两个断点之间
    断点包括：无法匹配的 ')'，或虚拟起始点


"""