class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        return string == string[::-1]

# This solution has a time complexity of O(d), where d is the number of digits in the integer x.
# The algorithm converts the integer to a string and checks if the string is equal to its reverse.
# Both the conversion to string and the reversal operation take linear time relative to the number of digits