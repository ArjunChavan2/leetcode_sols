class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1 = len(s1) + 1
        l2 = len(s2) + 1
        memo = [[0 for i in range(l2)] for j in range(l1)]
        
        for i in range(1, l1):
            memo[i][0] = ord(s1[i - 1]) + memo[i - 1][0]
        for j in range(1, l2):
            memo[0][j] = ord(s2[j - 1]) + memo[0][j - 1]
        
        for i in range(1, l1):
            for j in range(1, l2):                
                if s1[i - 1] == s2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                else:
                    memo[i][j] = min(memo[i - 1][j] + ord(s1[i - 1]), memo[i][j - 1] + ord(s2[j - 1]))

        return memo[-1][-1]
    
# a 97
# b 98
# c 99
# d 100
# e 101
# f 102
# g 103
# h 104
# i 105
# j 106
# k 107
# l 108
# m 109
# n 110
# o 111
# p 112
# q 113
# r 114
# s 115
# t 116
# u 117
# v 118
# w 119
# x 120
# y 121
# z 122

# This solution runs in O(m * n) time and space complexity where m and n are the lengths of the input strings s1 and 
# s2 respectively. This is because it uses a dynamic programming approach with a 2D memoization table of size m+1 and
# n+1 to store the minimum ASCII delete sums for substrings of s1 and s2. The algorithm iterates through each character
# of both strings, filling in the memoization table based on whether the characters match or not. The space complexity is 
# also O(m * n) due to the storage of the memoization table.