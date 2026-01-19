class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # build(l, r)：用 nums[l..r] 构造一棵平衡 BST，返回根节点
        def build(l: int, r: int) -> Optional[TreeNode]:
            if l > r:                 # 区间为空
                return None
            # floor divide
            mid = (l + r) // 2        # 取中点作为根（保证尽量平衡）
            root = TreeNode(nums[mid])

            # 左半部分构造左子树，右半部分构造右子树
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)

            return root

        return build(0, len(nums) - 1)





"""
Docstring for AdvancedDataStructureAndGraph.BinaryTree.sortedArrayToBST

在数据结构中，平衡二叉搜索树（Balanced Binary Search Tree，简称 BBST） 是二叉搜索树（BST）的一种优化版本。
它的核心目的是通过“平衡”机制，防止树退化成链表，从而保证操作的高效性。

1. 为什么需要平衡二叉搜索树
    在普通的二叉搜索树中，如果插入的数据是有序的，
    树可能会退化成一个链表，导致查找、插入和删除操作的时间复杂度从 O(log n) 变为 O(n)。
    为了避免这种情况，平衡二叉搜索树通过各种平衡机制，确保树的高度保持在 O(log n) 范围内，
    从而保证所有基本操作的时间复杂度均为 O(log n)。

2. 平衡二叉搜索树的定义
一棵树要被称为平衡二叉搜索树，通常需要满足两个条件：

    符合 BST 性质： 左子树所有节点的值 < 根节点的值 < 右子树所有节点的值。

    符合平衡性质： 任意节点的左子树和右子树的**高度差（平衡因子）**
        不能超过 1（这是 AVL 树的标准，不同类型的平衡树有不同的平衡定义）。

3. 常见的平衡二叉搜索树类型
    AVL 树： 通过旋转操作来保持树的平衡，确保每个节点的平衡因子在 -1 到 1 之间。
    红黑树： 通过节点的颜色（红色或黑色）和特定的规则来保持树的平衡，确保从根到叶子的最长路径不超过最短路径的两倍。
    B 树： 主要用于数据库和文件系统，允许节点有多个子节点，从而减少树的高度，提高访问效率。 


是不是所有的递归算法都能转化为迭代算法？
"""