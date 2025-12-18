class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLength = 0
        currentLength = 0
        uniques = set()
        c = 0
        while c < len(s):
            if s[c] in uniques:
                print(c)
                longestLength = max(longestLength, currentLength)
                c = c - currentLength + 1
                uniques = set(s[c])
                currentLength = 1
            else:
                uniques.add(s[c])
                currentLength += 1
            print(c)
            c += 1
        return max(longestLength, currentLength)
    
# This solution has a time complexity of O(n^2) in the worst case
# because the while loop can potentially reset the pointer 'c' multiple times,
# leading to repeated traversals of the string. However, it correctly finds
# the length of the longest substring without repeating characters.