from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 1) 记录每个字符最后出现的位置
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        res = []
        start = 0  # 当前片段起点
        end = 0    # 当前片段最远边界（必须至少到这里）

        # 2) 扫描字符串，动态扩展 end
        for i, ch in enumerate(s):
            end = max(end, last[ch])  # 当前字符要求片段至少覆盖到 last[ch]

            # 3) 当扫描到 end，说明可以切分一个片段
            if i == end:
                res.append(end - start + 1)
                start = i + 1  # 开启下一个片段

        return res

"""
Docstring for CoreAlgorithmicIdeasAndTechnique.GreedyAlgorithm.partitionLabels

算法思路（贪心）
    预处理：用字典 last 记录每个字符在字符串中最后一次出现的下标。
    扫描字符串，维护当前片段：
        start：当前片段起点
        end：当前片段必须覆盖到的最远位置（初始为当前字符的 last）
    对每个位置 i：
        更新 end = max(end, last[s[i]])
        如果 i == end，说明从 start 到 end 之间出现的所有字符，其最后出现位置都不超过 end，因此可以安全切分：
            片段长度 = end - start + 1
            更新 start = i + 1 开始下一个片段

"""
