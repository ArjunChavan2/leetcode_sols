class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        ret = 0
        for i in range(0, len(columnTitle)):
            ret += (ord(columnTitle[i]) - ord('A') + 1)*26**i
        
        return ret

# This solution runs in O(n) time complexity, where n is the length of the input string columnTitle.
# It uses O(1) space complexity, as it only requires a constant amount of additional space to store the 
# variables ret and i.