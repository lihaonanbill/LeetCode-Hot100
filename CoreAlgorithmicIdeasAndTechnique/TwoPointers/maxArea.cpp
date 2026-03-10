#include<vector>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& height) {
        // 左指针，从最左端开始
        int left = 0;

        // 右指针，从最右端开始
        int right = height.size() - 1;

        // 用来保存遍历过程中出现的最大面积
        int ans = 0;

        // 当 left 与 right 相遇时，说明所有可能情况都考虑过了
        while (left < right) {
            // 木桶能装多少水，取决于较短的那根板子
            int h = min(height[left], height[right]);

            // 宽度就是两条线之间的距离
            int w = right - left;

            // 当前这对边形成的面积
            int area = h * w;

            // 更新最大值
            ans = max(ans, area);

            // 贪心思想：
            // 谁短就移动谁，因为短板决定当前高度
            // 如果移动较高的一边，宽度变小了，但高度上限不变，不可能更优
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        // 返回最大面积
        return ans;
    }
};