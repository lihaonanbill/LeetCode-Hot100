#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // 用来存储所有满足条件的不重复三元组
        vector<vector<int>> res;
        int n = nums.size();

        // 先将数组排序
        // 排序后可以使用双指针，并且更容易去重
        sort(nums.begin(), nums.end());

        // 枚举三元组中的第一个数 nums[i]
        for (int i = 0; i < n - 2; i++) {
            // 剪枝：
            // 如果当前 nums[i] 已经大于 0，
            // 后面两个数也一定 >= nums[i]，三数之和不可能为 0
            if (nums[i] > 0) {
                break;
            }

            // 去重：
            // 如果当前 nums[i] 和前一个一样，
            // 那么以它作为第一个数得到的三元组会重复
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            // 双指针初始化
            int left = i + 1;
            int right = n - 1;

            // 在区间 [i+1, n-1] 中寻找两个数
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                // 找到一个和为 0 的三元组
                if (sum == 0) {
                    res.push_back({nums[i], nums[left], nums[right]});

                    // 去重：
                    // 跳过所有与当前 left 相同的值
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }

                    // 去重：
                    // 跳过所有与当前 right 相同的值
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }

                    // 继续寻找下一组
                    left++;
                    right--;
                }
                else if (sum < 0) {
                    // 当前和太小，需要增大和
                    // 因为数组有序，所以 left 右移
                    left++;
                }
                else {
                    // 当前和太大，需要减小和
                    // 因为数组有序，所以 right 左移
                    right--;
                }
            }
        }

        // 返回所有结果
        return res;
    }
};
/*
res.push_back()的参数需要用{}括起来，表示这是一个初始化列表。
res.push_back({nums[i], nums[left], nums[right]});


*/