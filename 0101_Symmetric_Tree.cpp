
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
    bool check(TreeNode* nodeL, TreeNode *nodeR)
    {
        if(nodeL && nodeR)
        {
            return nodeL->val == nodeR->val && check(nodeL->left, nodeR->right) && check(nodeR->left, nodeL->right);
        }
        if(!nodeL && !nodeR)
            return true;
        return false;
    }

    bool isSymmetric(TreeNode* root) {
        return check(root->left, root->right);
    }
};

/* This solution runs in O(n) time complexity where n is the number of nodes in the tree, and uses O(h) space
    complexity where h is the height of the tree. The space complexity is due to the recursion stack which can
    go a max of as deep as the height of the tree.
*/