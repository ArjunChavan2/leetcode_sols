from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums) // 2
        if(len(nums) == 0):
            return None
        root = TreeNode(val = nums[mid])
        del nums[mid]

        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid::])
        
        return root

# This solution runs in O(n) time complexity, where n is the length of the input list nums. The space complexity
# is O(log n) due to the recursive call stack used in the function. The function works by finding the middle element 
# of the list and using it as the root of the tree. It then recursively applies the same process to the left and right
# halves of the list, creating the left and right subtrees of the root node. The function continues to do this until the
# input list is empty, at which point it returns None. The resulting tree is a binary search tree, where the left child of
# each node has a value less than the parent node's value, and the right child has a value greater than the parent node's value.