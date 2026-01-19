from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional['ListNode']) -> Optional['ListNode']:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next is not None and prev.next.next is not None:
            a = prev.next
            b = a.next

            # 交换 a 和 b
            a.next = b.next
            b.next = a
            prev.next = b

            # prev 移动到下一对之前
            prev = a

        return dummy.next


"""
T:O(n)
S:O(1)


"""