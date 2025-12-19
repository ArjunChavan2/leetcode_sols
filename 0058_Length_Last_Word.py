class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])
        
# This solution runs in O(n) time complexity, where n is the length of the input string. 
# The split() function splits the string into a list of words, and the [-1] index accesses 
# the last word in the list. The len() function then returns the length of that word.