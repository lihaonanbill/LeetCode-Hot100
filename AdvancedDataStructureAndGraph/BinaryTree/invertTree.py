
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # 交换左右子树
        root.left, root.right = root.right, root.left

        # 递归翻转子树
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        q = deque([root])
        while q:
            node = q.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root


"""
个人初步想法：BFS算法中把visit改成交换左右节点
q.deque([root])等价于
    q = deque()
    q.append(root)


    deque是怎么实现的，

"""