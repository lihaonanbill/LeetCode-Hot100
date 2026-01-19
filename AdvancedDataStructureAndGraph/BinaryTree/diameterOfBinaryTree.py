class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # ans 记录当前发现的最大直径（按“边数”）
        ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            """
            返回：以 node 为根的子树高度（按“节点数”计）
            例如叶子节点高度=1，空节点高度=0
            """
            nonlocal ans
            if node is None:
                return 0

            # 后序：先算左右子树高度
            left_h = dfs(node.left)
            right_h = dfs(node.right)

            # 以当前节点为“拐点”的路径长度（边数）= 左高度 + 右高度
            # 因为 left_h/right_h 是节点数口径，拼起来刚好得到边数
            ans = max(ans, left_h + right_h)

            # 返回当前子树高度（节点数口径）
            return 1 + max(left_h, right_h)

        dfs(root)
        return ans














"""
Docstring for AdvancedDataStructureAndGraph.BinaryTree.diameterOfBinaryTree

对于每个node，如果最长路径绕过它，那么路径长度就是：
    左子树最大深度+右子树最大深度
用DFS返回“从当前节点向下走到最深叶子”的高度，并在遍历过程中不断更新全局最大值

空节点高度=0





nonlocal ans

nonlocal：修改外层函数的变量（嵌套函数用）

global：修改全局变量（模块级变量）

"""


