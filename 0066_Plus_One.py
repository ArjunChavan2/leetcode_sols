class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        digits = list(str(int("".join(digits))+1))
        for i in range(len(digits)):
            digits[i] = int(digits[i])
        return digits

# This solution runs in O(n) time complexity, where n is the length of the input list 'digits'.
# It first converts all the elements in 'digits' to strings and then joins them together to form a single string.
# It then converts the string to an integer, adds 1 to it, and converts it back to a string.
# Finally, it converts each character in the string back to an integer and returns the resulting list.