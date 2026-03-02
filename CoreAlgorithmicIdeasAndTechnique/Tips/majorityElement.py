from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore 投票算法：
        两两抵消非候选元素与候选元素的票数，最终留下的候选即多数元素。
        题目保证多数元素一定存在。
        """
        candidate = None
        count = 0

        for x in nums:
            if count == 0:
                # 票数归零，重新选择候选人
                candidate = x
                count = 1
            elif x == candidate:
                # 同票：支持票 +1
                count += 1
            else:
                # 异票：抵消一票
                count -= 1

        return candidate