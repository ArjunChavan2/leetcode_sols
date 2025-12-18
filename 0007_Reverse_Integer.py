class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            str_x = str(x)[::-1]
            if int(str_x) > 2**31 - 1:
                return 0
        else:
            str_x = "-" + str(-1*x)[::-1]
            if int(str_x) * -1 > 2**31 - 1:
                return 0
        return int(str_x)

# This solution has a time complexity of O(d), where d is the number of digits in the integer x.
# The reversal of the integer is done by converting it to a string and reversing that string,
# which takes linear time relative to the number of digits. The subsequent checks and conversions
# also operate in linear time with respect to the number of digits.