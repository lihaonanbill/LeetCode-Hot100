from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next          # 一次走 1 步
            fast = fast.next.next     # 一次走 2 步
            if slow is fast:          # 指向同一节点则说明有环
                return True

        return False
"""


为什么有环就一定会相遇:因为快慢指针之间的距离每一步减少一个单位

T: O(n)
S: O(1)


"""