from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        p1, p2 = list1, list2

        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next

        # 把剩余部分直接接上
        tail.next = p1 if p1 else p2
        return dummy.next
    



def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


if __name__ == "__main__":
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])

    result = Solution().mergeTwoLists(l1, l2)
    print_list(result)   # 期望输出：[1, 1, 2, 3, 4, 4]
"""
T:O(m+n)
S:O(1)

"""