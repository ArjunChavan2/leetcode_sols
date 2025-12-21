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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p && q)
        {
            return p->val == q->val and isSameTree(p->left, q->left) and isSameTree(p->right, q->right);
        }
        if(p == nullptr and q == nullptr)
            return true;
        return false;
    }
};

/*This solution runs in O(n) time complexity and O(1) space complexity. The solution uses recursion to compare the
 values of the nodes in the two trees. If the values are equal, it recursively calls itself to compare the left 
 and right subtrees. If the values are not equal, it returns false. If both nodes are null, it returns true. If 
 one node is null and the other is not, it returns false. This solution works for all valid inputs.
*/