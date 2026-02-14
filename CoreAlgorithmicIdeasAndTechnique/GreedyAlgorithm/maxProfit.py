from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_price: 迄今为止见过的最低价格（最佳买入点）
        min_price = float("inf")
        # best: 最大利润
        best = 0

        for p in prices:
            # 如果今天卖出，能得到的利润
            best = max(best, p - min_price)
            # 更新最低买入价（必须在卖出计算之后/之前都行，这里放后面更直观）
            min_price = min(min_price, p)

        return best


"""
Docstring for CoreAlgorithmicIdeasAndTechnique.GreedyAlgorithm.maxProfit
算法思路

一次遍历，维护两个量：
    min_price：到当前天为止出现过的最低买入价
    best：当前能获得的最大利润
遍历每天价格 p：
    如果今天卖出，利润是 p - min_price
    用它更新 best
    再用 p 更新 min_price（为未来可能的卖出做准备）
这样保证“先买后卖”，并且只做一次交易。

"""
