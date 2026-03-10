#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // 哈希表：
        // key   -> 排序后的字符串
        // value -> 所有具有相同排序结果的原字符串
        unordered_map<string, vector<string>> mp;

        // 遍历每一个字符串
        for (const string& s : strs) {
            // 复制一份字符串，用于排序后作为哈希表的键
            string key = s;
            sort(key.begin(), key.end());

            // 将原字符串放入对应分组
            mp[key].push_back(s);
        }

        // 把哈希表中的所有分组提取到结果数组中
        vector<vector<string>> ans;
        for (auto& p : mp) {
            ans.push_back(p.second);
        }

        return ans;
    }
};