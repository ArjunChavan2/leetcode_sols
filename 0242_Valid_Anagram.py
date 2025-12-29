class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for c in 'abcdefghijklmnopqrstuvwxyz':
            counter[c] = 0
        for c in s:
            counter[c] += 1
        for c in t:
            counter[c] -= 1
        
        if(min(counter.values()) == 0 and max(counter.values()) == 0):
            return True
        return False

# This solution runs in O(n) time complexity where n is the length of the input strings s and t. This is because it
# iterates through both strings once to count the occurrences of each character, which takes O(n) time. 
# The space complexity is O(1) because the size of the counter dictionary is fixed (26 letters in the English alphabet)
# regardless of the input size. Therefore, the overall space complexity is O(1).