class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

# This solution has a time complexity of O((n-m+1) * m) in the worst case,
# where n is the length of the haystack string and m is the length of the needle
# string. This is because for each of the (n-m+1) possible starting positions
# in the haystack, the algorithm may need to compare up to m characters to
# check for a match with the needle.