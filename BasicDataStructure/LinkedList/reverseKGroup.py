from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional['ListNode'], k: int) -> Optional['ListNode']:
        # 哑节点
        dummy = ListNode(0, head)
        # 每一组翻转前的前驱节点
        group_prev = dummy


        while True:
            # 1) 找到这一组的第 k 个节点 kth
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next  # 剩余不足 k 个，不翻转

            group_next = kth.next  # 下一组起点

            # 2) 翻转当前组：从 group_prev.next 到 kth
            # cur当前节点，prev当前节点未来指向的节点(我觉得就不该用prev)，nxt保存当前节点本来指向的节点
            prev = group_next
            cur = group_prev.next
            while cur is not group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # 3) 接回去
            old_group_head = group_prev.next  # 翻转前的头，翻转后变尾
            group_prev.next = kth             # kth 翻转后是新头
            group_prev = old_group_head       # 下一组的前驱

        # 理论上不会到这里
"""

T:O(n)
S:O(1)

"""