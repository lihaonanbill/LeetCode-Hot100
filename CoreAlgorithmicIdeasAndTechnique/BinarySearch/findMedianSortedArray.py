
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保证 nums1 是更短的数组，二分更省
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B = B, A
            m, n = n, m

        total = m + n
        half = (total + 1) // 2  # 左半部分需要的元素数量（奇数时左边多一个）

        left, right = 0, m  # i 的可选范围是 [0, m]

        while left <= right:
            i = (left + right) // 2
            j = half - i

            # 处理越界，用正负无穷兜底
            A_left  = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i]     if i < m else float("inf")
            B_left  = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j]     if j < n else float("inf")

            # 检查切分是否满足“左边都 <= 右边”
            if A_left > B_right:
                # i 太大，左移
                right = i - 1
            elif B_left > A_right:
                # i 太小，右移
                left = i + 1
            else:
                # 找到正确切分
                if total % 2 == 1:
                    return float(max(A_left, B_left))
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0

        # 理论上不会走到这里（输入满足题意）
        return 0.0



"""
Docstring for CoreAlgorithmicIdeasAndTechnique.BinarySearch.findMedianSortedArray

算法思路（二分“切分点”）
    设 A=nums1，B=nums2，长度分别为 m,n。我们在 更短的数组 A 上二分一个切分位置 i，对应 B 的切分位置 j 由总左侧元素个数决定：
        总长度 total = m + n
        左侧需要元素个数 half = (total + 1) // 2（确保奇数时左侧多一个）
        选定 i 后，j = half - i
    切分后比较四个边界值：
        A_left = A[i-1]（若 i==0 取 -∞）
        A_right = A[i]（若 i==m 取 +∞）
        B_left = B[j-1]（若 j==0 取 -∞）
        B_right = B[j]（若 j==n 取 +∞）
    目标条件（正确切分）：
    A_left≤B_right且B_left≤A_right
        若 A_left > B_right：说明 i 太大，左移 right = i - 1
        若 B_left > A_right：说明 i 太小，右移 left = i + 1
        否则找到正确切分：
            若 total 为奇数：中位数 = max(A_left, B_left)
            若 total 为偶数：中位数 = (max(A_left,B_left) + min(A_right,B_right)) / 2


T:O(log(min(m,n)))
S:O(1)



这里又是左右都闭合
我试了一下，如果把
    left, right = 0, m改为left, right = 0, m+1
    left <= right改为left < right
    right = i - 1改为right = i
也能通过
"""