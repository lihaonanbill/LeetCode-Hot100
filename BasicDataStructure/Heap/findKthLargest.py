from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Quickselect (平均 O(n)) 找第 k 大元素。
        第 k 大 <=> 升序第 (n-k) 小（0-based target 下标）。
        """
        n = len(nums)
        target = n - k  # 升序排序后的目标下标

        left, right = 0, n - 1

        while left <= right:
            # 随机选枢轴，避免最坏情况在某些输入上频繁出现
            pivot = nums[random.randint(left, right)]

            # 三路划分:
            # nums[left:lt] < pivot
            # nums[lt:i] == pivot
            # nums[gt+1:right+1] > pivot
            lt, i, gt = left, left, right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            # 现在 [left, lt-1] < pivot, [lt, gt] == pivot, [gt+1, right] > pivot
            if target < lt:
                right = lt - 1
            elif target > gt:
                left = gt + 1
            else:
                return pivot

        # 题目保证 k 合法，理论上不会走到这里
        raise ValueError("Invalid input")

"""
Docstring for BasicDataStructure.Heap.findKthLargest

算法思路（Quickselect + 三路划分）
    第 k 大 = 按升序排序后下标为 n - k 的元素（0-based）。
    随机选一个 pivot。
    做 三路划分（Dutch National Flag）：
        < pivot 放左边
        == pivot 放中间
        > pivot 放右边
    划分后：
        若目标下标 target 在左段：继续在左段找
        在中段：直接返回 pivot
        在右段：继续在右段找
    迭代直到找到。
三路划分对重复元素特别稳，不容易退化

Q:
上面的算法和堆有什么关系？
A:
没关系

needs proof

区间,状态,含义
"[left, lt-1]",已确认,里面全是比 pivot 小的数（左侧领地）。
"[lt, i-1]",已确认,里面全是等于 pivot 的数（中间领地）。
"[i, gt]",未探索,“迷雾区”，i 还没扫描到的数。
"[gt+1, right]",已确认,里面全是比 pivot 大的数（右侧领地）。

第一步：i = 0, nums[0] = 3
判断：3 == pivot
操作：属于中间区域，i 直接向右移。
数组：[3, 5, 2, 3, 1]
状态：lt = 0, i = 1, gt = 4

第二步：i = 1, nums[1] = 5
判断：5 > pivot
操作：把 5 扔到最右边。交换 nums[i] 和 nums[gt]（即 5 和 1 交换）。
注意：gt 向左移，但 i 不动（因为换回来的 1 还没检查过）。
数组：[3, 1, 2, 3, 5]
状态：lt = 0, i = 1, gt = 3

第三步：i = 1, nums[1] = 1
判断：1 < pivot
操作：把 1 换到左边。交换 nums[i] 和 nums[lt]（即 1 和 3 交换）。
结果：lt 和 i 都向右移。
数组：[1, 3, 2, 3, 5]
状态：lt = 1, i = 2, gt = 3

第四步：i = 2, nums[2] = 2
判断：2 < pivot
操作：把 2 换到左边。交换 nums[i] 和 nums[lt]（即 2 和第一个 3 交换）。
数组：[1, 2, 3, 3, 5]
状态：lt = 2, i = 3, gt = 3

第五步：i = 3, nums[3] = 3
判断：3 == pivot
操作：相等，i 直接向右移。
数组：[1, 2, 3, 3, 5]
状态：lt = 2, i = 4, gt = 3



"""