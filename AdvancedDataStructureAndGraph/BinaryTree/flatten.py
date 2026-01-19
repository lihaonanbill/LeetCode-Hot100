"""
Docstring for AdvancedDataStructureAndGraph.BinaryTree.flatten

20260118
题目要求：二叉树展开为单链表，单链表与二叉树先序遍历顺序相同。

个人思路：毫无思路>_<


"""

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None  # 指向已经展开好的链表的头（前驱）

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal prev
            if not node:
                return

            # 关键：先处理右子树，再处理左子树（反前序）
            dfs(node.right)
            dfs(node.left)

            # 把当前节点的 right 指向 prev（把链表接起来）
            node.right = prev
            # 左指针必须置空（题目要求）
            node.left = None

            # 更新 prev：当前节点成为新的链表头
            prev = node

        dfs(root)


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if cur.left:
                # 找左子树的最右节点（前驱）
                pre = cur.left
                while pre.right:
                    pre = pre.right

                # 把当前的右子树接到 pre 的右边
                pre.right = cur.right

                # 左子树搬到右边
                cur.right = cur.left
                cur.left = None

            # 继续处理下一个节点（链表方向）
            cur = cur.right



"""

解法 1：递归（后序，从后往前接）
    先把左右子树都展开，再把当前节点接到“已经展开好的链表头”前面。
    用一个指针 prev 记录“当前已经展开好的链表的头节点”（实际上是前驱）。

    处理顺序：右子树 → 左子树 → 根（反前序），这样最后链表就是前序（根→左→右）。

时间：O(n)（每个节点访问一次）
空间：O(h)（递归栈，h 为树高；最坏 O(n)）


解法 2：进阶 O(1) 额外空间（Morris 思想）
对每个节点 cur：
    如果 cur.left 存在：
        找到 cur.left 的最右节点 pre（前驱）
        把 pre.right 指向 cur.right（把原右子树接到左子树最右边）
        再把 cur.right 指向 cur.left，并令 cur.left = None
    然后 cur = cur.right 继续
这样就把“左子树整体搬到右边”，并保持前序顺序。

时间：O(n)（每条边最多走几次，总体线性）
空间：O(1)（不算递归栈，因为没有递归）


"""