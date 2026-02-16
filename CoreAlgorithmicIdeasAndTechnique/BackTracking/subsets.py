from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        path: List[int] = []

        def dfs(start: int) -> None:
            # 当前 path 本身就是一个子集，加入答案
            res.append(path.copy())

            # 尝试从 start 开始选择后续元素加入子集
            for i in range(start, len(nums)):
                path.append(nums[i])     # 选择 nums[i]
                dfs(i + 1)               # 递归处理后面的元素
                path.pop()               # 撤销选择（回溯）

        dfs(0)
        return res

"""
算法思路（回溯 / 选或不选 DFS）
    用一个路径 path 表示当前构造的子集。
    从下标 start 开始枚举下一个要加入子集的元素：
        把当前 path 先加入答案（因为任何前缀都是一个合法子集）
        然后依次尝试把 nums[i] 加入 path，递归到 i+1，回来后再撤销（回溯）。
    这样就能生成所有子集（幂集），且不重复。    

时空复杂度
设 n = len(nums)
    时间复杂度：
        共有 2^n个子集；每次 path.copy() 最坏复制 O(n)。
        所以总时间为O(n⋅2^n)。
    空间复杂度：
        递归深度最多 n，路径 path 最多 n：额外栈空间 O(n)。
        但如果把返回结果 res 也算上，存储所有子集需要 O(n⋅2^n)。

res.append(path.copy()),为什么要用path.copy()而不直接用path
    因为 path 在回溯过程中会变回 []
    而 res 中保存的是对同一个 path 对象的引用
    当 path 最终变为 [] 时，res 中所有引用都指向同一个 []

eg: [1,2,3]
             []
           /  |  \
         [1] [2] [3]
        /  \    \
    [1,2] [1,3] [2,3]
      /
  [1,2,3]

"""