from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        返回 nums 的所有全排列（nums 中元素互不相同）。
        """
        res: List[List[int]] = []
        path: List[int] = []
        used = [False] * len(nums)  # used[i] = True 表示 nums[i] 已经在 path 中

        def backtrack() -> None:
            # 终止条件：当前排列长度等于 nums 长度，得到一个完整排列
            if len(path) == len(nums):
                res.append(path.copy())  # 必须 copy，否则后续回溯会修改 path
                return

            # 尝试把每个没用过的元素放到当前空位
            for i in range(len(nums)):
                if used[i]:
                    continue
                # 选择
                used[i] = True
                path.append(nums[i])

                # 递归到下一层
                backtrack()

                # 撤销选择（回溯）
                path.pop()
                used[i] = False

        backtrack()
        return res





"""
Docstring for AdvancedDataStructureAndGraph.BackTracking.permute
算法思路
    把“构造排列”看成在填 n 个位置：
        第 1 个位置可以放 n 个数中的任意一个
        第 2 个位置放剩下的 n-1 个
        ……直到放满
    用 path 存当前构造的排列，用 used 防止同一个数被重复使用。
    每次递归代表“确定一个位置”，当 path 长度达到 n 就收集答案。

时空复杂度
    设 n = len(nums)：
    时间复杂度：共有 n! 个排列，每个排列需要拷贝长度 n 的列表O(n⋅n!)
    额外空间复杂度（不算输出 res）：递归栈深度 n，used 和 path 都是 O(n)
    （如果把输出也算上，结果本身就是 O(n⋅n!) 规模。）

复制问题需要注意
res.append(path.copy())  # 必须 copy，否则后续回溯会修改 path

"""