# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# This solution runs in O(n) time complexity, where n is the number of nodes in the tree.
# It also uses O(n) space complexity due to the recursion stack and the space required to store the result list.
# Inorder traversal visits nodes in the order left child, root, right child. This function traverses the tree in that
# order recursively and returns a list of node values in the correct order.