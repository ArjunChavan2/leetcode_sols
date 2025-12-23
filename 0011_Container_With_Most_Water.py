from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)

        left = 0
        right = l - 1
        currMax = (right - left) * min(height[left], height[right])

        for i in range(0, len(height)):
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
            currMax = max(currMax,(right - left) * min(height[left], height[right]))
        
        return currMax

# This solution runs in O(n) runtime and uses O(1) space. This is because it users a two-pointer approach to traverse the
# list and only uses a constant amount of extra space for variables. Unlike a brute-force approach that would check all
# possible pairs of lines (O(n^2) time complexity), this method increases the left pointer when it is the limiting factor
# to the container height and decreases the right pointer otherwise, ensuring that all potential maximum areas are considered
# efficiently.