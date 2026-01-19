from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional['ListNode'], n: int) -> Optional['ListNode']:
        # 哑节点，如果删除头节点也能统一处理
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # fast 先走 n 步
        for _ in range(n):
            fast = fast.next

        # fast 和 slow 同时走，直到 fast 到最后一个节点
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        # 删除 slow 后面的那个节点（倒数第 n 个）
        slow.next = slow.next.next

        return dummy.next
"""

快慢指针+哑节点

 for _ in range(n): 是什么意思
"""