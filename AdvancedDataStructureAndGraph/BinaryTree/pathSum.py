"""
Docstring for AdvancedDataStructureAndGraph.BinaryTree.pathSum

没思路>_<
"""


from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # cnt[p]：在“当前从根到正在访问节点的路径上”，前缀和为 p 出现的次数
        cnt = defaultdict(int)
        cnt[0] = 1  # 空路径前缀和=0，用于统计从根开始的路径

        def dfs(node: Optional[TreeNode], curSum: int) -> int:
            if node is None:
                return 0

            # 1) 更新前缀和：加入当前节点值
            curSum += node.val

            # 2) 以当前节点为终点，满足 targetSum 的路径条数
            #    需要 prevSum = curSum - targetSum
            res = cnt[curSum - targetSum]

            # 3) 将当前前缀和加入哈希表（进入该节点）
            cnt[curSum] += 1

            # 4) 继续向下搜索（路径必须向下）
            res += dfs(node.left, curSum)
            res += dfs(node.right, curSum)

            # 5) 回溯：离开该节点，撤销当前前缀和的记录（避免左右子树互相影响）
            cnt[curSum] -= 1

            return res

        return dfs(root, 0)

"""
chatgpt思路：
算法思路（前缀和 + 计数）

从根走到当前节点的路径和记为 curSum（前缀和）。
如果某条向下路径（从某个祖先的下一个节点开始，到当前节点结束）和为 targetSum，则：

curSum - prevSum = targetSum ⇒ prevSum = curSum - targetSum

所以我们用哈希表 cnt 记录“当前根到当前节点路径上，各个前缀和出现的次数”。
遍历到一个节点时：
    更新 curSum
    把 cnt[curSum - targetSum] 加到答案（表示以当前节点为终点的合法路径数）
    cnt[curSum] += 1（把当前前缀和加入路径）
    递归左右子树
    回溯 cnt[curSum] -= 1（离开该节点，撤销影响）

    

时空复杂度

设节点数为 n，树高为 h：
    - 时间复杂度：O(n)
        每个节点只进行常数次哈希访问/更新。

    - 空间复杂度：O(h)（平均）
        递归栈深度为 h，哈希表中同时有效的前缀和也最多 h 个；最坏退化链表为 O(n）。

没搞懂
搞懂了！好一个前缀和

Q&A
cnt = defaultdict(int)
    创建一个字典，默认值是 0
    当你访问一个不存在的 key 时，它会自动返回 0，而不是报错。

为什么 cnt[0] = 1 ？
    这是为了处理从根节点开始的路径。如果路径和正好等于 targetSum，那么 curSum - targetSum = 0。
    因此，我们需要预先在 cnt 中记录前缀和为 0 出现过一次，以便正确统计从根节点开始的路径。






"""
