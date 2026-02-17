from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 建图：b -> a，表示学完 b 才能学 a
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        # 把所有入度为 0 的课程入队：这些课程不依赖任何前置课
        q = deque([i for i in range(numCourses) if indeg[i] == 0])

        taken = 0  # 已“学完”的课程数量

        # BFS 拓扑排序
        while q:
            cur = q.popleft()
            taken += 1

            # cur 学完后，它的后继课程入度 -1
            for nxt in graph[cur]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)

        # 能否学完 = 是否能拓扑排序出所有节点
        return taken == numCourses

"""
Docstring for AdvancedDataStructureAndGraph.GraphTheory.canFinish

算法思路（拓扑排序 / 入度 BFS）
    每个先修关系 [a, b] 表示：学 a 之前要先学 b
        等价于一条有向边：b -> a
    统计每门课的入度 indeg[a]（还有多少前置课没完成）
    把所有 入度=0 的课程先入队（这些课可以直接学）
    每次从队列取出一门课 cur：
        表示学完了它
        对它指向的后续课程 nxt：indeg[nxt] -= 1
        如果某门课入度减到 0，就入队
    最后如果学到的课程数 taken == numCourses，说明不存在环，能学完；否则有环。


进入while循环必须要有没有prerequisites的course,因此对于只有环的情况一定会返回False

"""