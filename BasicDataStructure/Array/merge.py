from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        合并所有重叠的区间，返回不重叠区间数组（覆盖原输入所有区间）。
        """

        # 1) 边界情况：空输入直接返回
        if not intervals:
            return []

        # 2) 按区间起点排序（起点相同则按终点排序，便于处理）
        intervals.sort(key=lambda x: (x[0], x[1]))

        # 3) 用结果数组保存合并后的区间
        merged: List[List[int]] = []
        cur_start, cur_end = intervals[0]  # 当前正在合并的区间

        # 4) 线性扫描：尝试把后续区间合并进当前区间
        for start, end in intervals[1:]:
            if start <= cur_end:
                # 有重叠/相接：扩展当前区间的右端点
                cur_end = max(cur_end, end)
            else:
                # 无重叠：把当前区间放入结果，并开启新区间
                merged.append([cur_start, cur_end])
                cur_start, cur_end = start, end

        # 5) 别忘了把最后一个正在合并的区间加入结果
        merged.append([cur_start, cur_end])

        return merged
"""
算法思路
    排序：把所有区间按起点从小到大排序（起点相同按终点）。
    扫描合并：  
        维护一个“当前合并区间” [cur_start, cur_end]
        对每个新区间 [start, end]：
            若 start <= cur_end，说明与当前区间重叠或相接（题目示例把 [1,4] 和 [4,5] 视为可合并），更新 cur_end = max(cur_end, end)
            否则无重叠：把当前区间加入答案，并令当前区间变为新区间
    扫描结束后把最后的当前区间加入答案。

T: O(nlogn)
S: O(n)




Q:
intervals.sort(key=lambda x: (x[0], x[1]))?
A:
就地排序，确定排序次序
Q:为什么叫lamda

"""