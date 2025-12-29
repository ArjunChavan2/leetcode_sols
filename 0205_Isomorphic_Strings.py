class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        
        for i in range(0, len(s)):
            dic[s[i]] = t[i]
        
        if(len(set(dic.values())) != len(dic.values())):
            return False
        #Multiple keys point to one value

        for i in range(0, len(s)):
            s = s[0:i] + dic[s[i]] + s[i+1::]
        return s == t

# This solution runs in O(n) time complexity where n is the length of the input strings s and t. This is because it
# iterates through the strings a constant number of times: once to build the mapping dictionary and once to construct 
# the new string based on the mapping. Therefore, the overall time complexity is O(n). The space complexity is also O(n) in the worst case,
# as the dictionary may store a mapping for each unique character in the string, leading to up to n entries in the dictionary.