from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups 用来存放分组结果
        groups = defaultdict(list)
        for s in strs:
            # key : 排序后的字符串()
            # 将字符串s的字符排序
            # 以排序后的字符串作为“特征键”
            key = ''.join(sorted(s))
            # 将原字符串s放入对应分组 
            groups[key].append(s)

        return list(groups.values())

"""


输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

defaultdict(list)的作用：
    普通 dict：如果 key 不存在，访问会报错 KeyError
    defaultdict(list)：如果 key 不存在，会自动创建一个空列表 [] 作为默认值
list(groups.values())的作用：
    groups.values() 会拿到 所有 value（所有分组列表）
    返回的是一个“视图对象”（dict_values），不是普通 list。
    list(...) 是把这个视图对象转换成真正的列表，符合题目要求 List[List[str]]
    e.g.
    groups.values()         # dict_values([["eat","tea","ate"], ["tan","nat"], ["bat"]])
    list(groups.values())   # [["eat","tea","ate"], ["tan","nat"], ["bat"]]

时空复杂度：
    时间复杂度：
        n = len(strs)（字符串个数
        k 为字符串平均长度（题目中 k <= 100）
        sorted(s) 排序需要 O(k log k)''.join(...) 需要 O(k)
        字典插入/查找均摊 O(1)，append 均摊 O(1)
        O(n⋅(klogk+k))=O(n⋅klogk)
    空间复杂度：
        哈希表里存放所有字符串引用：O(n)
        每次生成的 key 长度为 k，总体 key 的存储规模在最坏情况下约 O(nk)
        排序时的临时空间：O(k)


"""

