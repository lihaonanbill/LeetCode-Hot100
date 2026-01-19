from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 1) 快慢指针找到中点（slow 最终在中间附近）
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 如果 fast 不为空，说明长度为奇数，slow 需要再走一步跳过中点
        if fast:
            slow = slow.next

        # 2) 反转后半段链表
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # prev 是反转后后半段的头

        # 3) 从头和“反转后的后半段”同时走，逐个比较
        p1, p2 = head, prev
        while p2:  # 后半段长度 <= 前半段，所以以 p2 为准
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True
"""
T:O(n)
S:O(1)



if not head or not head.next: 是不是只需要not head.next这一个判断标准就够了

"""