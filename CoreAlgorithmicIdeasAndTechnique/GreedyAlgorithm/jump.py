from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0          # 已使用的跳数
        end = 0            # 当前这一次跳跃所能覆盖到的最远边界
        farthest = 0       # 扫描当前边界内所有点后，下一次跳跃可达的最远位置

        # 注意：遍历到 n-2 即可，因为到达/越过 n-1 就不需要再跳
        for i in range(n - 1):
            # 在当前层内，更新下一层最远可达位置
            farthest = max(farthest, i + nums[i])

            # 到达当前层边界：必须进行一次跳跃，进入下一层
            if i == end:
                jumps += 1
                end = farthest

                # 已经可以覆盖到最后一个位置，提前结束
                if end >= n - 1:
                    break

        return jumps

"""
Docstring for CoreAlgorithmicIdeasAndTechnique.GreedyAlgorithm.jump

算法思路（Greedy / 层级遍历）
    把数组下标看成图的节点，从 i 可以到达 [i+1, i+nums[i]]。
    我们不真正建图，而是用两个边界模拟 BFS 的“层”：
        end：当前跳数能到达的最远边界（当前层的右边界）
        farthest：在遍历当前层 [0..end] 的过程中，能扩展到的下一层最远位置
        当遍历到 i == end，说明当前层扫描完了，需要 跳一次，并把 end = farthest
    题目保证能到达最后一位。

T: O(n)
S: O(1)

正确性使用数学归纳法证明
"""
