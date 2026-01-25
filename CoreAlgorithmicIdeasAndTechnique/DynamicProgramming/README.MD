#### 目录

1. 70.climbStairs
    - DP
2. 118.generate
    - 杨辉三角
3. 198.rob
4. 279.numSquares
    - 完全背包问题
    - 广度优先(还没弄)
5. 322.coinChange
    - 感觉和上面这题好像
    - 广度优先?
6. 139.wordBreak
    - 字典树?,记忆化搜索,数组，哈希表，字符串，动态规划
7. 300.LengthOfLIS
    - array，binary search，DP
    - 0215-0310(260125)
    - why?
8. 152.maxProduct
    - array, dp
    - 1746-1802(260125)
    - 这题思路挺简单
9. 416.canPartition
    - array, dp
    - 2008-2141(260125)
    - 0/1背包
    - 这题有点懵
10. 32.longestValidParentheses
    - 栈，字符串，动态规划


#### 动态规划的定义
- 最优子结构 (Optimal Substructure)： 问题的最优解可以由其子问题的最优解推导出来。
    - 例子： 从北京到上海的最短路径，如果经过南京，那么这条路径必然也包含了“南京到上海”的最短路径。
- 重叠子问题 (Overlapping Subproblems)： 在递归求解过程中，相同的子问题会被多次计算。
    - 例子： 计算斐波那契数列 F(5) 需要计算 F(4) 和 F(3)，而计算 F(4) 又需要计算 F(3)。这里的 F(3) 就是重叠子问题。


