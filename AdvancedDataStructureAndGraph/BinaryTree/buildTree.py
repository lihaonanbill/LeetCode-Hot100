"""
Docstring for AdvancedDataStructureAndGraph.BinaryTree.buildTree

从前序与中序遍历序列构造二叉树



"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 把中序遍历的值 -> 下标存起来，方便 O(1) 找根的位置
        idx = {val: i for i, val in enumerate(inorder)}

        pre_i = 0  # 当前处理到 preorder 的哪个位置

        def build(l: int, r: int) -> Optional[TreeNode]:
            """
            用 inorder[l..r] 这段区间构造子树，返回子树根节点
            """
            nonlocal pre_i
            if l > r:  # 区间为空，没有节点
                return None

            # 前序遍历的当前元素就是这棵子树的根
            root_val = preorder[pre_i]
            pre_i += 1
            root = TreeNode(root_val)

            # 在中序中找到根的位置，从而划分左右子树
            mid = idx[root_val]

            # 注意：先构造左子树，再构造右子树（符合前序：根-左-右）
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)

            return root

        return build(0, len(inorder) - 1)
"""

算法思路（递归分治 + 哈希表）
    关键性质：
        前序 preorder：第一个元素一定是当前子树的根
        中序 inorder：根左边是左子树，根右边是右子树    
    做法：  
        先用哈希表 idx[val] = val 在 inorder 中的位置，O(1) 找根位置
        用指针 pre_i 指向当前要用的前序位置：
            取 preorder[pre_i] 作为根，然后 pre_i += 1
        在 inorder 的区间 [l, r] 内递归构造：
            根在 mid = idx[root_val]
            左子树区间 [l, mid-1]
            右子树区间 [mid+1, r]

时空复杂度

设节点数为 n：

    时间复杂度：O(n)
    每个节点创建一次，查 index 是 O(1)。

    空间复杂度：O(n)
    哈希表 idx 是 O(n)，递归栈是 O(h)（最坏 O(n)）。

    

字典推导式（Dictionary Comprehension）
idx = {val: i for i, val in enumerate(inorder)}
"""