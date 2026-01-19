# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        cur = root

        while cur is not None or stack:
            # 1) 一路向左，把路径压栈
            while cur is not None:
                stack.append(cur)
                cur = cur.left

            # 2) 弹出栈顶：当前未处理的最小节点
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val

            # 3) 转向右子树继续中序
            cur = node.right

        # 题目保证 1 <= k <= 节点数，一般走不到这里
        return -1




"""
算法思路（中序遍历 + 计数）

    BST 的中序遍历结果是严格递增序列。
    所以我们做中序遍历（左→根→右），每访问一个节点就把 k 减 1，当 k == 0 
    时当前节点就是第 K 小。

为了避免递归栈，也为了能更直观“走左链”，用显式栈做迭代中序。（什么意思）

T: O(h + k)，h 是树的高度
S: O(h)



个人想法：
    如果BST是中序遍历 严格递增，那么做一遍中序遍历是不是就行


"""
if __name__ == "__main__":
    # 示例用法
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    k = 1
    solution = Solution()
    result = solution.kthSmallest(root, k)
    print(result)  # 输出: 1