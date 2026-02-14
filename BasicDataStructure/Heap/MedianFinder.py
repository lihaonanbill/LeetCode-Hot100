
import heapq

class MedianFinder:
    def __init__(self):
        # small: max-heap (用负数实现)，保存较小的一半
        self.small = []
        # large: min-heap，保存较大的一半
        self.large = []

    def addNum(self, num: int) -> None:
        """
        插入一个数，并维护：
        1) small 的大小 = large 或者 = large + 1
        2) small 中元素都 <= large 中元素
        """
        # 1) 先放进 small（大顶堆，用负数）
        heapq.heappush(self.small, -num)

        # 2) 为保证 small 的最大值 <= large 的最小值：
        #    把 small 堆顶(最大)搬到 large
        x = -heapq.heappop(self.small)
        heapq.heappush(self.large, x)

        # 3) 尺寸平衡：让 small 至少和 large 一样多（或多 1）
        if len(self.large) > len(self.small):
            y = heapq.heappop(self.large)
            heapq.heappush(self.small, -y)

    def findMedian(self) -> float:
        """
        返回当前中位数：
        - 奇数个：small 堆顶
        - 偶数个：small 堆顶与 large 堆顶平均
        """
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0

"""

算法思路（Two Heaps）

维护两部分数据：
small：大顶堆（存较小的一半），堆顶是这部分的最大值
Python 只有小顶堆，所以用取负数实现大顶堆
large：小顶堆（存较大的一半），堆顶是这部分的最小值
保持两个不变式：
len(small) 要么等于 len(large)，要么比它 多 1（让 small 负责“中位数”）
small 中所有元素 ≤ large 中所有元素（通过搬运堆顶维持）
这样：
如果总数为奇数：中位数是 small 的堆顶
如果总数为偶数：中位数是 small 堆顶和 large 堆顶的平均值

"""