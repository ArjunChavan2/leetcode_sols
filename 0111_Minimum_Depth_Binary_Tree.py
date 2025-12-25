from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 and right == 0:
            return 1
        if left == 0:
            return 1 + right
        if right == 0:
            return 1 + left
        return 1 + min(left, right)

# This solution runs in O(n) time complexity where n is the number of nodes in the binary tree. This is because it
# visits each node exactly once to compute the minimum depth. The space complexity is O(h), where h is the height
# of the tree, due to the recursions tack. In the worst case, for a skewed tree, the height can be n, 
# leading to O(n) space complexity.