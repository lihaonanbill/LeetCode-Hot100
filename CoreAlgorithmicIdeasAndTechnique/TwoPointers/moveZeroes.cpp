#include<vector>
using namespace std;
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int k = 0;  // 下一个非零元素应放的位置

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                // 只有当 i 和 k 不同时才交换，减少无效操作
                if (i != k) {
                    swap(nums[i], nums[k]);
                }
                k++;
            }
        }
    }
};
/**
这个版本的含义是：

    k 前面的区域始终是已经整理好的非零元素
    当扫描到一个非零元素时，把它交换到 k 位置
    因为前面可能有 0，所以交换后相当于把 0 往后送

例如：

    [0,1,0,3,12]
    遇到 1，和前面的 0 交换
    遇到 3，和前面的 0 交换
    遇到 12，和前面的 0 交换
    最后自然得到：
    [1,3,12,0,0]


T: O(n)
S: O(1)
 */