

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        动态规划 + 滚动数组（空间优化）
        dp[j] 表示：当前处理到 text1 的前 i 个字符时，与 text2 前 j 个字符的 LCS 长度
        """
        # 让 text2 更短，从而 dp 更小，节省空间
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)  # dp[0] = 0 表示 text2 为空

        for i in range(1, m + 1):
            prev = 0  # prev 保存 dp[i-1][j-1]（左上角）
            for j in range(1, n + 1):
                temp = dp[j]  # 暂存 dp[i-1][j]（上方），因为 dp[j] 马上要被覆盖
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])  # 上方 vs 左方
                prev = temp  # 更新 prev 为旧的 dp[i-1][j]
        return dp[n]
"""

算法思路（动态规划）
    1）状态定义
        令：
        dp[i][j] 表示 text1 前 i 个字符与 text2 前 j 个字符的最长公共子序列长度
        dp[i][j]=text1前i个字符与text2前j个字符的最长公共子序列长度
        这里的“前 i 个字符”指 text1[0:i]（不含 i）。

    2）状态转移
        如果当前字符相同：text1[i-1] == text2[j-1]
        dp[i][j]=dp[i−1][j−1]+1
        如果当前字符不同：
        dp[i][j]=max(dp[i−1][j], dp[i][j−1])
        解释：要么丢掉 text1 的最后一个字符，要么丢掉 text2 的最后一个字符。

    3）初始化
        当 i=0 或 j=0 时，至少有一个空串：
        dp[0][j]=dp[i][0]=0


Q:
1. 为什么让 text2 更短，从而 dp 更小，节省空间

T: O(mn)
S: O(min(m,n))


"""