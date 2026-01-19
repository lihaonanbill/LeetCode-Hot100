from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional['ListNode']) -> Optional['ListNode']:
        if head is None or head.next is None:
            return head

        # 计算长度
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        # dummy node
        dummy = ListNode(0, head)

        # 切分：从 head 开始切出长度为 size 的一段，返回下一段的起点
        def split(h: Optional['ListNode'], size: int) -> Optional['ListNode']:
            if h is None:
                return None
            for _ in range(size - 1):
                if h.next is None:
                    break
                h = h.next
            nxt = h.next
            h.next = None
            return nxt

        # 合并两个有序链表，返回 (合并后头, 合并后尾)
        def merge(a: Optional['ListNode'], b: Optional['ListNode']):
            d = ListNode(0)
            p = d
            while a and b:
                if a.val <= b.val:
                    p.next = a
                    a = a.next
                else:
                    p.next = b
                    b = b.next
                p = p.next
            p.next = a if a else b

            # 找到尾巴（用于下一次拼接）
            while p.next:
                p = p.next
            return d.next, p 
        
        step = 1
        while step < n:
            prev = dummy
            cur = dummy.next

            while cur:
                left = cur
                right = split(left, step)     # 切出右半段
                cur = split(right, step)      # 下一组的起点

                merged_head, merged_tail = merge(left, right)
                prev.next = merged_head
                prev = merged_tail

            step <<= 1  # step *= 2

        return dummy.next


"""
算法思路：自底向上归并
为什么时间复杂度是O(nlogn)/为什么归并排序的时间复杂度是O(nlogn)

step <<= 1  # step *= 2: <<符号是什么意思



"""