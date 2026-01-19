class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")  # 全局最大路径和（可能全为负）

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if node is None:
                return 0

            # 1) 先算左右子树“向上贡献”的最大值（后序）
            left_gain = dfs(node.left)
            right_gain = dfs(node.right)

            # 2) 如果子树贡献为负，就不要这条边（等价于取 0）
            left_best = max(0, left_gain)
            right_best = max(0, right_gain)

            # 3) 以当前节点为“拐点”的路径最大值：左 + node + 右
            ans = max(ans, node.val + left_best + right_best)

            # 4) 返回给父节点的值：只能选一条分支向上延伸
            return node.val + max(left_best, right_best)

        dfs(root)
        return ans
"""
我从下往上遍历每个节点：
    对每个节点，计算“如果路径在我这里拐弯，能有多大”，用它更新全局最大值
    同时，我只把“对父节点最有用的一条路”返回给父节点
    负数的路直接丢掉


"""