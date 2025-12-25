class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = "".join([item for item in s if item.isalnum()]).lower()
        t = len(l)
        for i in range(0, t // 2):
            if l[i] != l[t - i - 1]:
                return False
        return True

# This solution runs in O(n) time complexity where n is the length of the input string s. This is because it
# processes each character in the string once to filter and convert it to lowercase, which takes O(n) time.
# The subsequent palindrome check also takes O(n) time in the worst case, as it compares characters from the start 
# and end of the filtered string towards the center. Therefore, the overall time complexity is O(n). The space 
# complexity is also O(n) because the filtered string 'l' can potentially store all characters from the input string
# if they are all alphanumeric.