import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            # 堆元素是一个三元组(node.val, i, node),其中，i是为了node.val相同时可以打破平局
            if node:
                heapq.heappush(heap, (node.val, i, node))

        # 哑节点
        dummy = ListNode(0)
        # tail永远指向结果链表的最后一个节点
        tail = dummy


        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            # 把刚弹出节点的下一个节点”
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        tail.next = None
        return dummy.next



"""“
最大堆最小堆

完全二叉树

似乎有一个排序优先级，先是node.val然后是i然后是node
heapq.heappush(heap, (node.val, i, node))


"""