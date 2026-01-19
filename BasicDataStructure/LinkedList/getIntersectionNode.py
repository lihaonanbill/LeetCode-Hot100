from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB

        # 两指针分别走 A+B 和 B+A，总路程相同
        # 若有交点，会在交点相遇；若无交点，会同时走到 None
        while a is not b:
            # 当某个指针走到末尾None时, 把它切换到另一条链表的头
            a = a.next if a else headB
            b = b.next if b else headA

            # 完整写法
            # if a is not None:
            #     a = a.next
            # else:
            #     a = headB

            # if b is not None:
            #     b = b.next
            # else:
            #     b = headA


        return a
"""


is not; is; == 之间的区别是什么

T: 每个指针最多走m+n步, O(m+n)
S: 只用了两个指针变量，不使用额外数据结构，O(1)


"""