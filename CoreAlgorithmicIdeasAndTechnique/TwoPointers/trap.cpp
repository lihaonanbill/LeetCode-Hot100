#include<vector>
using namespace std;
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();

        // 双指针，分别指向当前还未处理区间的左右端点
        int left = 0;
        int right = n - 1;

        // leftMax 表示从左侧扫描到当前位置时，遇到的最高柱子
        int leftMax = 0;

        // rightMax 表示从右侧扫描到当前位置时，遇到的最高柱子
        int rightMax = 0;

        // 最终接到的总雨水量
        int ans = 0;

        while (left < right) {
            // 如果左边柱子更低，那么当前位置 left 的接水量
            // 只取决于 leftMax
            if (height[left] < height[right]) {
                // 当前柱子比 leftMax 还高，更新 leftMax
                if (height[left] >= leftMax) {
                    leftMax = height[left];
                } else {
                    // 当前柱子较矮，可以接水
                    ans += leftMax - height[left];
                }
                left++;
            } 
            // 否则处理右边
            else {
                // 当前柱子比 rightMax 还高，更新 rightMax
                if (height[right] >= rightMax) {
                    rightMax = height[right];
                } else {
                    // 当前柱子较矮，可以接水
                    ans += rightMax - height[right];
                }
                right--;
            }
        }

        return ans;
    }
};
/*
using namespace std;表示使用std命名空间，这样在代码中就可以直接使用vector、algorithm等
标准库中的类和函数，而不需要每次都写std::vecttor, std::sort等

*/