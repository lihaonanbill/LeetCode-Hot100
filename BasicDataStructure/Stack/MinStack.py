class MinStack:
    def __init__(self):
        """
        stack:     存所有元素
        min_stack: 与 stack 同步，每个位置存“到该位置为止的最小值”
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # 1) 正常入栈
        self.stack.append(val)

        # 2) 同步维护最小值栈
        if not self.min_stack:
            # 第一个元素时，最小值就是它本身
            self.min_stack.append(val)
        else:
            # 当前最小值 = min(新元素, 之前最小值)
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        """
        题目保证 pop/top/getMin 都在非空栈上调用
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



"""
Docstring for BasicDataStructure.Stack.MinStack

算法思路（Two Stacks）
    维护两个栈：
        stack：正常存放所有入栈元素
        min_stack：在每个位置同步存放“到当前为止的最小值”
    规则：
        push(x)：
            stack.append(x)
            min_stack.append(min(x, min_stack[-1]))（若 min_stack 为空则直接 append(x)）
        pop()：
            两个栈都 pop（同步出栈）
        top()：返回 stack[-1]
        getMin()：返回 min_stack[-1]
        这样任意时刻栈内最小值就是 min_stack 栈顶

时空复杂度
设当前栈内元素个数为 n：
    时间复杂度：
    push/pop/top/getMin 均为 O(1)
    空间复杂度：
    两个栈都可能存 n 个元素 ⇒ O(n)


"""

