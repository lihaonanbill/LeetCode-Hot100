class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], low, high) -> bool:
            # 空节点是有效 BST
            if node is None:
                return True

            # 当前节点必须严格落在 (low, high) 之间
            if (low is not None and node.val <= low) or (high is not None and node.val >= high):
                return False

            # 左子树：上界变为 node.val
            # 右子树：下界变为 node.val
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, None, None)
"""
算法思路（上下界约束）
    BST 的正确条件不是只看“父子大小”，而是：
        对任意节点 x：
        它左子树所有值都必须 < x.val
        它右子树所有值都必须 > x.val
    所以递归时要给每个节点带上允许的范围 (low, high)：
        左子树范围变为 (low, x.val)
        右子树范围变为 (x.val, high)
    任何节点不在范围内就返回 False.




T: O(n)
S: O(h)

"""