from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # 存下标，保持 nums[dq] 单调递减
        res = []

        for i, x in enumerate(nums):
            # 1) 移除窗口左侧已经滑出的下标（过期）
            # 当前窗口左边界是 i-k+1，所以 <= i-k 的都过期
            while dq and dq[0] <= i - k:
                dq.popleft()

            # 2) 维护单调递减：把所有比当前值小/等的队尾元素踢掉
            # 因为它们未来不可能成为最大值（被 x “支配”）
            while dq and nums[dq[-1]] <= x:
                dq.pop()

            # 3) 当前下标入队
            dq.append(i)

            # 4) 窗口形成后（i >= k-1），队头就是最大值
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res

"""
Docstring for String.Substring.maxSlidingWindow

算法思路（单调递减队列）
用一个双端队列 dq 存 下标，并保持队列对应的值 从队头到队尾单调递减：
对每个位置 i：
    弹出过期元素：如果队头下标 dq[0] <= i-k，说明不在当前窗口 [i-k+1, i] 内，弹出。
    维护单调性：当队尾元素 nums[dq[-1]] <= nums[i] 时，队尾弹出（因为它不可能再成为未来窗口最大值）。
    把当前下标 i 入队。
    当 i >= k-1 时，窗口形成，当前窗口最大值就是 nums[dq[0]]（队头最大）。

"""