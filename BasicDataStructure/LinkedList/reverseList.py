from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 已经反转好的部分的头
        prev = None
        # 当前正在处理的节点
        cur = head

        while cur:
            nxt = cur.next      # 暂存下一节点，防止断链
            cur.next = prev     # 反转指针方向
            prev = cur          # prev 前进
            cur = nxt           # cur 前进

        return prev

"""

T:O(n)
S:O(1)

"""