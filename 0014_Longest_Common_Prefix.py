class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest = strs[0]
        for c in range(0, len(longest)):
            for word in strs[1::]:
                if(c >= len(word)):
                    return longest[0:c]
                if word[c] != longest[c]:
                    return longest[0:c]
        
        return longest

# This solution has a time complexity of O(m * n), where m is the length of the shortest string in the list and n is the number of strings.
# The algorithm compares each character of the shortest string with the corresponding characters of all other strings.
# In the worst case, it may need to compare all characters of the shortest string with all other strings, leading to a quadratic relationship between the number of strings and the length of the shortest string