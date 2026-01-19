from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 空树直接返回空列表
        if root is None:
            return []

        res = []
        q = deque([root])  # 队列里存当前待处理的节点

        while q:
            level = []
            size = len(q)  # 当前层的节点数量（固定）

            # 这一轮只处理当前层的 size 个节点
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)

                # 把下一层节点入队
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # 当前层收集完毕
            res.append(level)

        return res


















"""
Docstring for AdvancedDataStructureAndGraph.BinaryTree.levelOrder


初步想法 bfs

"""

