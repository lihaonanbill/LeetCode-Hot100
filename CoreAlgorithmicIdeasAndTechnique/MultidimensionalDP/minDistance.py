class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        动态规划 + 滚动数组（空间优化）
        dp[j] 表示：当前处理到 word1 前 i 个字符时，变成 word2 前 j 个字符的最小编辑距离
        """
        # 让 word2 更短，减少 dp 数组长度，节省空间
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        m, n = len(word1), len(word2)

        # dp[j] = dp[0][j]：空串 -> word2[:j] 需要插入 j 次
        dp = list(range(n + 1))

        for i in range(1, m + 1):
            prev = dp[0]      # prev = dp[i-1][0]
            dp[0] = i         # dp[i][0]：word1[:i] -> 空串，删除 i 次

            for j in range(1, n + 1):
                temp = dp[j]  # 暂存 dp[i-1][j]（上方），dp[j] 即将被覆盖

                if word1[i - 1] == word2[j - 1]:
                    # 字符相同：继承左上角
                    dp[j] = prev
                else:
                    # 三种操作取最小：
                    # 删除：temp = dp[i-1][j]
                    # 插入：dp[j-1] = dp[i][j-1]
                    # 替换：prev = dp[i-1][j-1]
                    dp[j] = 1 + min(temp, dp[j - 1], prev)

                prev = temp  # 更新 prev 为下一格需要的 dp[i-1][j-1]

        return dp[n]
    

"""
算法思路（动态规划）
把 word1 变成 word2，允许三种操作（每次代价 1）：
    插入
    删除
    替换
    1) 状态定义
    dp[i][j] = 把 word1 的前 i 个字符变成 word2 的前 j 个字符的最小操作数
    其中：
        word1[1:i] 表示前 i 个字符
        word2[1:j] 表示前 j 个字符
    2) 初始化
        dp[0][j] = j：空串变成长度 j 的串，只能插入 j 次
        dp[i][0] = i：长度 i 的串变成空串，只能删除 i 次
    3) 状态转移
    考虑 word1[i-1] 和 word2[j-1]：
    如果相等：不需要操作 dp[i][j] = dp[i - 1][j - 1]
    如果不相等：取三种操作最小值 + 1
        删除（删掉 word1 的末尾字符）
            dp[i][j] = dp[i - 1][j] + 1
        插入（在 word1 末尾插入一个字符，使其匹配 word2[j-1]）
            dp[i][j] = dp[i][j - 1] + 1
        替换（把 word1[i-1] 替换为 word2[j-1]）
            dp[i][j] = dp[i - 1][j - 1] + 1
综合：
plaintext
          | dp[i - 1][j - 1],                          若 word1[i - 1] = word2[j - 1]
dp[i][j] = |
          | 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]), 否则

Q: 为什么不相等的时候，是取三种操作最小值+1

    
 """