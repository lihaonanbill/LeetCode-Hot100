
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []
        q = deque([root])

        while q:
            size = len(q)  # 当前层节点数
            for i in range(size):
                node = q.popleft()

                # 当前层的最后一个节点，就是右视图看到的节点
                if i == size - 1:
                    res.append(node.val)

                # 先左后右入队
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res



"""
Docstring for AdvancedDataStructureAndGraph.BinaryTree.rightSideView




个人想法：
    首先得比较以下左右子树高度
    其次对局部得树做广度优先进栈，每一层最后一个节点就是右视图节点就是栈顶节点

chatgpt想法：(和我差不多)
算法思路（BFS 层序遍历）
    按层遍历二叉树：每一层从左到右扫描，该层最后一个节点就是从右侧能看到的节点。
    做法：
        用队列 BFS
        每层先记录 size = len(queue)
        处理这一层的 size 个节点，最后一个弹出的节点加入答案

时间复杂度：O(n)（每个节点进队出队一次）

空间复杂度：O(w)（队列最多存一层节点；最坏 O(n)）


"""



