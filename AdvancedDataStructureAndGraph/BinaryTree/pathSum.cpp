#include <unordered_map>
using namespace std;


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };


class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        unordered_map<long long, int> cnt;
        cnt[0] = 1;  // 前缀和为0出现1次（空路径），用于统计从根开始的路径

        return dfs(root, 0LL, (long long)targetSum, cnt);
    }

private:
    int dfs(TreeNode* node, long long curSum, long long target,
            unordered_map<long long, int>& cnt) {
        if (!node) return 0;

        curSum += node->val;

        // 以当前节点为终点，路径和为 target 的条数
        int res = 0;
        auto it = cnt.find(curSum - target);
        if (it != cnt.end()) res += it->second;

        // 把当前前缀和加入哈希表
        cnt[curSum]++;

        // 继续往下搜索
        res += dfs(node->left, curSum, target, cnt);
        res += dfs(node->right, curSum, target, cnt);

        // 回溯：撤销当前节点的前缀和记录
        cnt[curSum]--;

        return res;
    }
};

/*

算法思路（前缀和 + 计数哈希）

从根到当前节点的一条路径上，设：
    curSum = 从根到当前节点的路径和（前缀和）
    若存在某个祖先前缀和 prevSum，使得  
    curSum - prevSum = targetSum
    那么从“prevSum 后一个节点”到当前节点这段路径和就是 targetSum。

所以我们用哈希表 cnt 记录：某个前缀和出现过多少次：
    初始 cnt[0] = 1（表示“空路径前缀和”为 0，方便从根开始的路径计数）
    DFS 到节点：
        更新 curSum += node->val
        本节点作为路径终点的贡献：cnt[curSum - target]
        把 curSum 加入哈希：cnt[curSum]++
        递归左右子树
        回溯：cnt[curSum]--（撤销当前节点对路径的影响）

时空复杂度
设节点数为 n，树高为 h：
    时间复杂度：O(n)
        每个节点只做常数次哈希操作。
    空间复杂度：O(h)（平均）
        递归栈是 O(h)，哈希表最多存从根到当前路径上的前缀和数量，也是 O(h)；最坏退化链表时 O(n)

Q: long long 和 int 范围各是多少
A: 
    int 范围：-2,147,483,648 到 2,147,483,647 （约 -2.1e9 到 2.1e9）
    long long 范围：-9,223,372,036,854,775,808 到 9,223,372,036,854,775,807 （约 -9.2e18 到 9.2e18）
Q: hash 表key值为什么用 long long

   
*/