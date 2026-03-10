#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // 用哈希集合存储所有数字，方便 O(1) 判断某个数字是否存在
        unordered_set<int> st(nums.begin(), nums.end());

        int ans = 0;  // 记录最长连续序列的长度

        // 遍历集合中的每个数字
        for (int x : st) {
            // 如果 x-1 存在，说明 x 不是连续序列的起点
            // 只有当 x-1 不存在时，x 才是起点
            if (st.count(x - 1)) {
                continue;
            }

            // 从 x 开始向后寻找连续的数字
            int cur = x;
            int len = 1;

            while (st.count(cur + 1)) {
                cur++;
                len++;
            }

            // 更新答案
            ans = max(ans, len);
        }

        return ans;
    }
};