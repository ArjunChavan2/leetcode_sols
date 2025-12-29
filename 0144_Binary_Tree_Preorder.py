from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trav(self, root, l):
        if(root == None):
            return
        l.append(root.val)
        self.trav(root.left, l)
        self.trav(root.right, l)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        self.trav(root, l)
        return l

# This solution runs in O(n) time complexity where n is the number of nodes in the binary tree. This is because it
# visits each node exactly once to perform the preorder traversal. The space complexity is O(h), where h is the height
# of the tree, due to the recursion stack. In the worst case, for a skewed tree, the height can be n, 
# leading to O(n) space complexity.