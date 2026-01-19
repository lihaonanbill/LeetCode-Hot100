# recursion
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # isMirror(a, b)：判断以 a、b 为根的两棵树是否互为镜像
        def isMirror(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            # 1) 两个都空：镜像成立
            if a is None and b is None:
                return True

            # 2) 一个空一个不空：结构不对称
            if a is None or b is None:
                return False

            # 3) 值不同：不对称
            if a.val != b.val:
                return False

            # 4) 递归检查“外侧”和“内侧”：
            #    a.left  要对应 b.right（外侧）
            #    a.right 要对应 b.left （内侧）
            return isMirror(a.left, b.right) and isMirror(a.right, b.left)

        # 空树默认对称
        if root is None:
            return True

        # 从根的左右子树开始做镜像判断
        return isMirror(root.left, root.right)


"""
T: O(n)
S: O(h)

"""


# iterated
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 空树对称
        if root is None:
            return True

        # 队列里存的是“需要互相比较是否镜像”的节点对 (a, b)
        # 初始要比较的是 root 的左子树根 和 右子树根
        q = deque([(root.left, root.right)])

        while q:
            # 取出一对节点进行比较
            a, b = q.popleft()

            # 1) 都为空：这一对对称，继续处理其它对
            if a is None and b is None:
                continue

            # 2) 一个空一个不空：结构不对称，直接 False
            if a is None or b is None:
                return False

            # 3) 值不同：不对称
            if a.val != b.val:
                return False

            # 4) 把下一层需要比较的“镜像位置”节点对入队
            #    外侧：a.left  对 b.right
            #    内侧：a.right 对 b.left
            q.append((a.left, b.right))
            q.append((a.right, b.left))

        # 所有节点对都通过检查，说明对称
        return True





"""

T: O(n)
S: O(w)

q = deque([(root.left, root.right)])
等价于
q = deque()
q.append((root.left, root.right))


"""




