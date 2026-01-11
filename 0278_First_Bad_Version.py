# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass
class Solution:
    def firstBadVersion(self, n: int) -> int:
        def binSearch(low, high):
            if high == low + 1:
                return high

            mid = (low + high) // 2
            if isBadVersion(mid):
                return binSearch(low, mid)
            return binSearch(mid, high)
    
        return binSearch(0, n)

# This solution runs in O(log n) time and O(log n) space complexity where n is the number of versions. This is because it uses
# a binary search to efficiently narrow down the range of version in half each iteration until it finds the first bad version
# which is stored in the variable high. The space complexity is O(1) since it uses a constant amount of extra space for the 
# recursive calls since this uses tail recursion. However, Python isn't optimized for tail recursion, so in practice, the 
# space complexity could be considered O(log n) due to the call stack.