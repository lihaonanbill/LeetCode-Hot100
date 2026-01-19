class Node:
    """双向链表节点：保存 (key, val) 以及前后指针。"""
    def __init__(self, key=0, val=0):
        self.key = key        # 关键：淘汰节点时需要用 key 从哈希表里删除
        self.val = val        # 缓存的值
        self.prev = None      # 前驱指针
        self.next = None      # 后继指针


class LRUCache:
    """
    LRU = 哈希表 + 双向链表
    - 哈希表：key -> Node，O(1) 定位节点
    - 双向链表：维护使用顺序
        head 之后：最近使用(MRU)
        tail 之前：最久未使用(LRU)
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}  # key -> Node

        # 两个哨兵节点（dummy head/tail），不存真实数据，只用来简化边界操作
        # 链表结构永远是：head <-> ...真实节点... <-> tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """把 node 从双向链表中摘除（O(1)）。"""
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _add_to_front(self, node: Node) -> None:
        """把 node 插入到 head 后面，使其成为“最近使用 MRU”（O(1)）。"""
        # 插入位置：head <-> (node) <-> 原 head.next
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node: Node) -> None:
        """命中/更新某个节点后，把它移动到最前面（变成 MRU）。"""
        self._remove(node)
        self._add_to_front(node)

    def _pop_lru(self) -> Node:
        """弹出并返回最久未使用节点（位于 tail.prev）（O(1)）。"""
        lru = self.tail.prev          # tail 前面的真实节点就是 LRU
        self._remove(lru)             # 从链表删除
        return lru

    def get(self, key: int) -> int:
        """
        1) 不存在：返回 -1
        2) 存在：返回值，并把该节点移动到最前（最近使用）
        """
        if key not in self.map:
            return -1

        node = self.map[key]          # O(1) 取到节点
        self._move_to_front(node)     # 访问过 -> 变成 MRU
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        1) key 已存在：更新 value，并移动到最前（最近使用）
        2) key 不存在：新建节点插到最前；若超容量，淘汰 LRU（链表尾部）
        """
        if key in self.map:
            node = self.map[key]
            node.val = value          # 更新值
            self._move_to_front(node) # 更新也算“使用过”
            return

        # 新 key：创建节点，加入哈希表 + 链表头部（MRU）
        node = Node(key, value)
        self.map[key] = node
        self._add_to_front(node)

        # 超容量：淘汰最久未使用 LRU
        if len(self.map) > self.cap:
            lru = self._pop_lru()     # 从链表移除 LRU
            del self.map[lru.key]     # 从哈希表删除对应 key



"""
算法思想：哈希表+双向链表
    用 字典 map：key -> 节点，实现 O(1) 定位

    用 双向链表维护访问顺序：
        链表头（靠近 head）= 最近使用 (MRU)
        链表尾（靠近 tail）= 最久未使用 (LRU)

    每次 get/put 命中某 key：把该节点移动到链表头

    超容量：删除链表尾部的 LRU 节点，并从 map 删除

    用两个哨兵节点 head, tail 简化边界处理。


T: O(1)
S: O(capacity)


"""