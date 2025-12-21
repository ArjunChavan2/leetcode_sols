mapping = {"2": "abc", "3": "def", "4": "ghi", "5":"jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9":"wxyz"}


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        ret = []

        def backtrack(index, curr):
            if index == len(digits):
                ret.append(curr[:])
                return
            
            for i in mapping[digits[index]]:
                curr += i
                backtrack(index + 1, curr)
                curr = curr[:-1]
        
        backtrack(0, "")
        return ret

# This solution runs in O(3^n * 4^m) time complexity, where n is the number of digits that map to 3 letters and m is 
# the number of digits that map to 4 letters. The space complexity is O(n + m) due to the recursion stack and the 
# current string being built. This solution uses backtracking to generate all possible combinations of letters for the
# given digits.