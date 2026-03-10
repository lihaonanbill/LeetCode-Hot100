#include <vector>      // 提供vector容器
#include <unordered_map> // 提供unordered_map容器
using namespace std;    // 使用std命名空间
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        // 哈希表：key = 数值, value = 数值对应的下标
        unordered_map<int,int> seen;

        // 遍历数组
        for (int i = 0; i < (int)nums.size(); ++i){

            // 计算当前数字需要的配对值
            int need = target - nums[i];

            // 在哈希表中查找 need 是否已经出现过
            if (seen.count(need)) {
                // 如果出现过，说明找到了答案
                return {seen[need], i};
            }

            // 如果没有找到，把当前数字存入哈希表
            // 记录该数字出现的位置
            seen[nums[i]] = i;
        }

        // 题目保证一定有解，这里只是语法需要
        // return {};
    }
};