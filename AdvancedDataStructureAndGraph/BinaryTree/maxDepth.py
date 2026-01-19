from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # 如果不写 self.，Python 会把 maxDepth 当作一个普通函数名去找（通常找不到，会报错）
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# DFS等价写法，不用self
class Solution:
    def maxDepth(self, root):
        def dfs(node):
            if not node:
                return 0
            return 1 + max(dfs(node.left), dfs(node.right))
        return dfs(root)


# BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = deque([root])
        depth = 0

        while q:
            size = len(q)          # 当前层节点数
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1             # 一层处理完

        return depth
    



"""


"""