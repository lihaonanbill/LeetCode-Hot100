from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # 排序用于剪枝
        res: List[List[int]] = []
        path: List[int] = []

        def dfs(start: int, remain: int) -> None:
            # 找到一组刚好凑成 target 的组合
            if remain == 0:
                res.append(path.copy())
                return

            # 从 start 开始选，保证组合按非降序生成，避免重复
            for i in range(start, len(candidates)):
                x = candidates[i]

                # 剪枝：后面只会更大，没必要继续
                if x > remain:
                    break

                path.append(x)          # 选择 x
                dfs(i, remain - x)      # i 不变 => 允许重复选择同一元素
                path.pop()              # 回溯撤销选择

        dfs(0, target)
        return res



"""
Docstring for AdvancedDataStructureAndGraph.BackTracking.combinationSum


算法思路（排序 + 回溯 + 剪枝）
    先排序 candidates，方便剪枝：当 candidates[i] > remain 时，后面更大，直接 break。
    用 path 记录当前组合，remain 记录还差多少到 target。
    递归函数 dfs(start, remain)：
        若 remain == 0：找到一组解，把 path 的拷贝加入答案。
        否则从 i = start 到末尾遍历：
            选择 candidates[i] 加入 path
            递归 dfs(i, remain - candidates[i])（注意仍是 i，表示可以重复选）
            回溯 pop() 撤销选择
    这样可以保证组合是非降序构造的，避免不同顺序导致的重复。


    
eg.[2,3,5] target=8
(0, 8) | []
├─ +2 → (0, 6) | [2]
│  ├─ +2 → (0, 4) | [2,2]
│  │  ├─ +2 → (0, 2) | [2,2,2]
│  │  │  └─ +2 → (0, 0) | [2,2,2,2]   ✅
│  │  ├─ +3 → (1, 1) | [2,2,3]        ✗ (后续 3/5 都 > 1，剪枝)
│  │  └─ +5 → (2,-1) | [2,2,5]        ✗ (剪枝：5 > 4 时其实不会走到这条)
│  ├─ +3 → (1, 3) | [2,3]
│  │  └─ +3 → (1, 0) | [2,3,3]        ✅
│  └─ +5 → (2, 1) | [2,5]            ✗ (后续只有 5，但 5 > 1，剪枝)
├─ +3 → (1, 5) | [3]
│  ├─ +3 → (1, 2) | [3,3]            ✗ (后续 3/5 都 > 2，剪枝)
│  └─ +5 → (2, 0) | [3,5]            ✅
└─ +5 → (2, 3) | [5]                ✗ (后续只有 5，但 5 > 3，剪枝)

"""

