from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 边界：空输入直接返回空列表
        if not digits:
            return []

        # 数字到字母的映射（电话按键）
        mp = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res: List[str] = []
        path: List[str] = []  # 用字符数组做路径，最后 ''.join(path)

        def dfs(idx: int) -> None:
            # 如果已经处理完所有数字，得到一个完整组合
            if idx == len(digits):
                res.append("".join(path))
                return

            # 当前数字对应的候选字母
            letters = mp[digits[idx]]
            for ch in letters:
                path.append(ch)     # 选择一个字母
                dfs(idx + 1)        # 处理下一位数字
                path.pop()          # 回溯撤销选择

        dfs(0)
        return res



"""
Docstring for AdvancedDataStructureAndGraph.BackTracking.letterCombinations



算法思路（回溯构造字符串）
    数字串 digits 的每一位都对应一组字母（2→abc，3→def ...）。
    我们从左到右逐位选择字母：
        递归到第 idx 位时，枚举该数字对应的每个字母加入路径 path
        当 idx == len(digits)，说明构造完成一个组合，加入答案
    如果 digits 为空，直接返回 []（题目要求）

res.append("".join(path))中的"".join(path)是开辟新的内存地址存入字符串吗
    是的
return 不加是不是也不影响
    不是，如果不加return,当idx==len(digits)的时候下面会下标溢出

"""


