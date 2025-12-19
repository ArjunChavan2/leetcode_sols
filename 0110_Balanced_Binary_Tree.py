# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:    
    def isBalanced(self, root: list[TreeNode]) -> bool:
        def heightBal(root):
            if(root == None):
                return [True, 0]

            hL = heightBal(root.left)
            hR = heightBal(root.right)
            h = 1 + max(hL[1], hR[1])
            return [hL[0] and hR[0] and abs(hL[1] - hR[1]) <= 1, h]
        return heightBal(root)[0]


# This solution runs in O(n) time complexity, where n is the number of nodes in the tree. It uses
# O(h) space complexity, where h is the height of the tree. The space complexity is due to the
# used by the recursion stack during the depth-first traversal of the tree. The solution checks if the
# tree is balanced by recursively calculating the height of the left and right subtrees and checking if
# the difference in height between the left and right subtrees is at most 1. If the difference in height is
# greater than 1, the tree is not balanced. The solution returns a boolean value indicating whether the tree is
# balanced or not.