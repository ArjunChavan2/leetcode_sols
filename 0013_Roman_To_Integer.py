class Solution:
    def romanToInt(self, s: str) -> int:
        tot = 0
        s = s[::-1]
        i = 0
        while i < len(s):
            if s[i] == "I":
                tot += 1

            if s[i] == "V":
                tot += 5
                if i < len(s) - 1 and s[i+1] == "I":
                    tot -=1
                    i += 1
            if s[i] == "X":
                tot += 10
                if i < len(s) - 1 and s[i+1] == "I":
                    tot -=1
                    i += 1
            
            if s[i] == "L":
                tot += 50
                if i < len(s) - 1 and s[i+1] == "X":
                    tot -=10
                    i += 1
            if s[i] == "C":
                tot += 100
                if i < len(s) - 1 and s[i+1] == "X":
                    tot -=10
                    i += 1

            if s[i] == "D":
                tot += 500
                if i < len(s) - 1 and s[i+1] == "C":
                    tot -=100
                    i += 1
            if   s[i] == "M":
                tot += 1000
                if i < len(s) - 1 and s[i+1] == "C":
                    tot -=100
                    i += 1
            i += 1
        return tot

# This solution has a time complexity of O(n), where n is the length of the input string s.
# The algorithm processes each character in the Roman numeral string exactly once,
# performing a constant amount of work for each character. Thus, the overall time complexity
# scales linearly with the size of the input.