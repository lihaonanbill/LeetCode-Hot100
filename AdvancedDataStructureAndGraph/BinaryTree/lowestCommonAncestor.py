"""
Docstring for AdvancedDataStructureAndGraph.BinaryTree.lowestCommonAncestor

没思路>_<
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 1) 终止条件：空节点
        if root is None:
            return None

        # 2) 如果当前节点就是 p 或 q，则直接返回当前节点
        #    （因为节点可以是自己的祖先）
        if root == p or root == q:
            return root

        # 3) 在左右子树中分别寻找 p 和 q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 4) 如果左右都找到了，说明 p 和 q 分别在两侧
        if left and right:
            return root

        # 5) 否则返回非空的一侧（都空则返回 None）
        return left if left else right
"""


时空复杂度

设节点数为 n，树高为 h：
    时间复杂度：O(n)（最坏需要遍历整棵树）
    空间复杂度：O(h)（递归栈；最坏退化链表为 O(n)

"""