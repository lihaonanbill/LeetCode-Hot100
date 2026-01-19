# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 存储读取到的值
        res = []
        # 栈
        stack = []
        cur = root

        while cur is not None or stack:
            # 1) 一路向左，把路径压栈
            while cur is not None:
                stack.append(cur)
                cur = cur.left

            # 2) 弹出栈顶，访问该节点
            node = stack.pop()
            res.append(node.val)

            # 3) 转向右子树
            cur = node.right

        return res



# 递归版本
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs(node.left)       # 左
            res.append(node.val) # 根
            dfs(node.right)      # 右

        dfs(root)
        return res

"""
Docstring for AdvancedDataStructureAndGraph.BinaryTree.inorderTraversal


先复习一下先，中，后序遍历(先中后指root的访问顺序)
先序遍历(pre-order traversal)
    root->left->right
中序遍历(in-order)
    left->root->right
后序遍历(post-order)
    left->right-root

    
栈里存的，永远是“左子树还没完全处理完的节点”
    压栈：表示“这个节点以后还要回来访问”
    出栈：表示“它的左子树已经全部搞定了，可以访问他了”
    
cur!=None: 说明还有路可以继续往下走
stack!=[]: 说明还有回头路没走完

只要还有节点没处理：
    能往左就一直往左，并记住路
    左边走完了，就回头访问一个节点
    然后去他的右边


    
对比递归：
    dfs(node):
        dfs(node.left)
        visit(node)
        dfs(node.right)



"""