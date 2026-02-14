from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1) 统计频次：num -> count
        freq = Counter(nums)  # O(n)

        # 2) 建桶：buckets[c] 存放所有出现次数为 c 的元素
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, c in freq.items():
            buckets[c].append(num)

        # 3) 从高频到低频收集答案
        res = []
        for c in range(n, 0, -1):
            if buckets[c]:
                res.extend(buckets[c])
                if len(res) >= k:
                    return res[:k]  # 题目允许任意顺序

        return res  # 理论上不会到这（k 合法）



"""
Docstring for BasicDataStructure.Heap.topKFrequent

思路 1：桶排序（Bucket Sort，推荐）
    先用哈希表统计每个数出现次数 freq[x]
    创建桶 buckets，下标表示“出现次数”，桶里放所有出现该次数的元素
        次数范围是 1..n，所以桶大小 n+1
    从高频到低频（从 n 到 1）扫桶，收集元素直到拿到 k 个

T:O(n)
S:O(n)

这是什么意思：
res.extend(buckets[c])

# 创建一个空列表
my_list = []
print(my_list)  # []

# 使用 extend() 添加另一个列表的元素
my_list.extend([1, 2, 3])
print(my_list)  # [1, 2, 3]

# 添加元组的元素
my_list.extend((4, 5))
print(my_list)  # [1, 2, 3, 4, 5]

# 添加字符串的元素（字符串也是可迭代的）
my_list.extend("ab")
print(my_list)  # [1, 2, 3, 4, 5, 'a', 'b']


lst = [1, 2]
lst.append([3, 4])   # 结果是 [1, 2, [3, 4]]

lst = [1, 2]
lst.extend([3, 4])   # 结果是 [1, 2, 3, 4]
"""
