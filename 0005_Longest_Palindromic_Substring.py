class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""

        for i in range(len(s)):
            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(ret):
                    ret = s[l:r+1]
            
                l-=1
                r+=1
            
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(ret):
                    ret = s[l:r+1]
            
                l-=1
                r+=1
        
        return ret

# This solution has a time complexity of O(n^2) in the worst case
# because for each character in the string, it potentially expands
# to check for palindromes, leading to a nested loop behavior. However,
# it correctly finds the longest palindromic substring in the input string.