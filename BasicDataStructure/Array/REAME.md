1. 53.maxSumArray
    - 动态规划
    - 动态规划感觉和前缀和有点像，chatgpt说两者数学上等价但是实现角度不同emmm，
    还有点小懵，但是没关系，才刚复习到这两个，还是在二叉树复习的，后面再理解
    三、真正的核心：DP 的“三要素”
2. 56.merge
    - 数组，排序
3. 189.rotate
    - 数组，数学，双指针
4. 238.productExceptSelf
    - 数组，前缀和
5. 41.firstMissingPositive
    - 数组，哈希表


# definition of DP
一个问题能否称为动态规划，取决于是否满足：
- 最优子结构（Optimal Substructure）
一个问题的最优解，可以由其子问题的最优解构成。
- 重叠子问题（Overlapping Subproblems）
子问题不是互相独立的，会被反复用到。
- 状态定义（State）
用一个变量（或一组变量）完整刻画子问题。

动态规划的本质不是公式，而是：
如何定义状态 + 如何从旧状态得到新状态。