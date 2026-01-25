from typing import List, Set

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        dp[i] 表示：s 的前 i 个字符（s[0:i]）能否被字典单词拼出来
        目标：dp[n]，n = len(s)

        转移：
          dp[i] = True 当且仅当存在 j < i，使得：
              dp[j] == True 且 s[j:i] 在字典中
        """
        # word_set: Set[str] 前面是变量名，后面是类型提示
        word_set: Set[str] = set(wordDict)  # 用集合加速查找 O(1) 平均
        n = len(s)

        # 优化：只需要尝试字典中出现过的单词长度
        lens = set(len(w) for w in word_set)
        max_len = max(lens) if lens else 0

        dp = [False] * (n + 1)
        dp[0] = True  # 空串一定可拼出（什么都不选）

        for i in range(1, n + 1):
            # 只尝试可能的长度 L，让 j = i - L
            for L in lens:
                j = i - L
                if j < 0:
                    continue
                # 如果前缀 s[0:j] 可拼出，并且 s[j:i] 是字典单词，则 dp[i]=True
                # s[j:i]左闭右开
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # 找到一种可行拆分即可提前结束，是的，这里只是确定 dp[i] 能否为 True

        return dp[n]
"""
s[i] vs dp[i] 
    s[i-1] 表示字符串 s 的第 i 个字符（0-based 索引）
    dp[i]True表示s[0,i-1]能被字典单词拼出来
    dp[0]是一个起始点，确保在if dp[j] and s[j:i] in word_set:的逻辑中，找到第一个单词时，j=0时能正确工作

T:
  最外层, n， 第二层K<20,s[j:i]切片 L  所以总时间复杂度是 O(n*K*L)

"""