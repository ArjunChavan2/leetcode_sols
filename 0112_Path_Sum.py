from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(root == None or abs(targetSum - root.val) < 0):
            return False
        
        if(root.val == targetSum and root.left == None and root.right == None):
            return True
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

# This solution runs in O(n) time complexity where n is the number of nodes in the binary tree. This is because it
# visits each node exactly once to check for the path sum. The space complexity is O(h), where h is the height
# of the tree, due to the recursion stack. In the worst case, for a skewed tree, the height can be n, 
# leading to O(n) space complexity.