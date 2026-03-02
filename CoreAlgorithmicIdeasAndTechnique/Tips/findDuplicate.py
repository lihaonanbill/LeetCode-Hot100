from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Floyd 判圈（快慢指针）
        不修改数组，O(1) 额外空间
        """
        # 1) 第一阶段：找到快慢指针相遇点（一定在环内）
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]          # 走一步
            fast = nums[nums[fast]]    # 走两步
            print(f"slow: {slow}, fast: {fast}")
            print(slow==fast)
            if slow == fast:
                break

        # 2) 第二阶段：从起点 0 和 相遇点 同步走，找到环入口
        p1 = nums[0]
        p2 = slow
        print(slow)
        while p1 != p2:
            # print(f"p1: {p1}, p2: {p2}")
            p1 = nums[p1]
            p2 = nums[p2]

        return p1  # 或 p2，都是重复数（环入口）


# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         # 第一阶段：找相遇点
#         slow = 0
#         fast = 0
#         while True:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#             if slow == fast:
#                 break

#         # 第二阶段：找入口
#         p1 = 0
#         p2 = slow
#         while p1 != p2:
#             p1 = nums[p1]
#             p2 = nums[p2]

#         return p1


if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate([1, 3, 4, 2, 2]))  # 输出: 2
    print(s.findDuplicate([3, 1, 3, 4, 2]))  # 输出: 3

"""

一、算法思路（把数组看成链表 + 判圈）
    题目条件：nums 长度为 n+1，元素取值在 [1, n]，且只有一个数重复（可能重复多次）。
    把下标当作节点，把“指向”定义为：next(i)=nums[i]
    由于 nums[i] ∈ [1,n]，所以从 0 出发：
        0 -> nums[0] -> nums[nums[0]] -> ...
        永远不会走到 0 以外的非法位置，必然在 1..n 中循环。
    因为有重复数，必然存在两个不同下标指向同一个值（入度≥2），这会导致链表结构出现“环”。
    重复数字就是环的入口。

二、Floyd 判圈两阶段
    阶段 1：找到相遇点
        slow 每次走 1 步：slow = nums[slow]
        fast 每次走 2 步：fast = nums[nums[fast]]
        它们一定会在环内相遇。
    阶段 2：找到环入口（重复数）
        让 p1 = 0，p2 = 相遇点
        两者每次都走一步：p1 = nums[p1], p2 = nums[p2]
        相遇位置就是环入口，也就是重复数。



Q:
为什么
    让 p1 = 0，p2 = 相遇点
    两者每次都走一步：p1 = nums[p1], p2 = nums[p2]
    相遇位置就是环入口，也就是重复数。


二、定义关键距离
    设：
    a = 从起点 0 到环入口的距离
    b = 从环入口到第一次相遇点的距离
    c = 环的长度
三、第一次相遇时的关系
    慢指针每次走 1 步
    快指针每次走 2 步
    假设慢指针走了：
    slow = a + b
    快指针走了：
    fast = 2(a + b)
    但快指针一定比慢指针多绕了若干圈：
    fast = a + b + k * c （k >= 1）
    因为：
    2(a + b) = a + b + k * c
    整理得：
    a + b = k * c
四、推导关键结论
    由：
    a + b = k * c
    得到：
    a = k * c - b
    写成：
    a = (c - b) + (k - 1) * c
五、解释这个式子的意义
    (c - b) = 从相遇点走回环入口的距离
    (k - 1) * c = 在环里多绕若干整圈
    在环里多绕整圈不影响最终位置。
    所以：
    从相遇点出发走 a 步，
    一定会回到环入口。
    同时：
    从起点出发走 a 步，
    也正好到环入口。
六、因此算法第二阶段成立
    让：
    p1 = 0
    p2 = 相遇点
    然后每次：
    p1 = nums[p1]
    p2 = nums[p2]
    它们都会走 a 步，
    并且会在“环入口”相遇。
    这个环入口，
    就是重复的数字。

bug:
    一开始的slow和fast与后来的p1的起点要设置相同
"""