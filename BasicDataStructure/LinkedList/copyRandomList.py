from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # 1) 复制节点并穿插到原链表中：A->B 变成 A->A'->B->B'
        cur = head
        while cur is not None:
            copy = Node(cur.val, cur.next, None)
            cur.next = copy
            cur = copy.next

        # 2) 设置复制节点的 random 指针,A'.random = A.random.next
        cur = head
        while cur is not None:
            copy = cur.next
            copy.random = cur.random.next if cur.random is not None else None
            cur = copy.next

        # 3) 拆分：恢复原链表，同时取出新链表
        cur = head
        new_head = head.next
        while cur is not None:
            copy = cur.next
            cur.next = copy.next
            copy.next = copy.next.next if copy.next is not None else None
            cur = cur.next

        return new_head


"""
easy
但是我的小脑瓜可想不出来

"""