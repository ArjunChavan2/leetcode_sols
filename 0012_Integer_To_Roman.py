class Solution:
    def intToRoman(self, num: int) -> str:
        conv = {'M' : 1000, 'CM' : 900, 'D': 500, "CD" : 400, "C" : 100, "C" : 100, "XC" : 90, "L" : 50, "XL" : 40, "X" : 10, "IX" : 9, "V" : 5, "IV" : 4, "I" : 1}

        ret = ""
        for key,val in conv.items():
            while num >= val:
                ret += key
                num -= val
        return ret

# This solution has a time complexity of O(1) because the number of Roman numeral symbols is fixed and limited.
# The algorithm iterates through a predefined set of Roman numeral values and constructs the Roman numeral representation
# of the given integer. Since the maximum value for the input integer is constrained (typically up to 3999 in standard Roman numeral systems),
# the number of iterations and operations performed does not scale with the size of the input, leading to constant time complexity.