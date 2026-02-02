class Solution:
    def decodeString(self, s: str) -> str:
        """
        用栈解码形如 k[encoded_string] 的字符串，支持嵌套与多位数字。
        """
        stack = []          # 存 (上一层的字符串列表 prev, 重复次数 k)
        cur = []            # 当前层正在构建的字符串（用 list 存字符/片段更高效）
        num = 0             # 当前读到的重复次数（可能多位）

        for ch in s:
            if ch.isdigit():
                # 多位数字：例如 "12[ab]" => num = 12
                num = num * 10 + (ord(ch) - ord('0'))
            elif ch == '[':
                # 进入新的一层：把当前层的状态保存起来
                stack.append((cur, num))
                # 重置，开始构建括号内的内容
                cur = []
                num = 0
            elif ch == ']':
                # 当前层结束：弹出上一层，并进行拼接
                prev, k = stack.pop()
                segment = ''.join(cur)   # 当前括号内完成的字符串
                # 回到上一层：prev + segment * k
                cur = prev + [segment * k]
            else:
                # 普通字母，直接加入当前层
                cur.append(ch)

        return ''.join(cur)



"""
Docstring for BasicDataStructure.Stack.decodeString


算法思路（Stack）
遍历字符串 s，维护：
    num：当前正在读取的重复次数（可能是多位数）
    cur：当前层（当前括号内/外）已构建的字符串（用列表存字符更高效）
    stack：保存进入 [ 之前的状态 (prev_str, repeat_k)
规则：
    遇到数字：更新 num = num * 10 + int(ch)
    遇到 [：把当前状态压栈 (cur, num)，然后重置 cur = []，num = 0
    遇到字母：追加到 cur
    遇到 ]：弹栈得到 (prev, k)，把当前 cur 变成字符串 segment，然后 cur = prev + segment * k
最终把 cur join 成结果。



时空复杂度
设最终解码后的字符串长度为 N（题目保证 N <= 1e5）：
    时间复杂度：O(N)
        每个字符（在输出中）被构造/复制的总量与最终输出规模同阶。
    空间复杂度：O(N)
        栈保存中间状态 + 构建输出所需空间。



ord()是什么:ascii码
''.join(cur)作用是什么：将列表中的字符串元素连接成一个字符串
    strings = ["hello", "world"]
    result = ' '.join(strings)  # "hello world"（用空格连接）
    result = '-'.join(strings)  # "hello-world"（用-连接）
    result = ''.join(strings)   # "helloworld"（直接拼接）

3[a2[c]]

"""


