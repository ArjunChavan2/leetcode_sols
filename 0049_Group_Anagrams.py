from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            currMap = {}
            for c in word:
                if c not in currMap:
                    currMap[c] = 1
                else:
                    currMap[c] += 1
            
            l = frozenset(currMap.items())
            if l not in d:
                d[l] = [word]
            else:
                d[l].append(word)


        return list(d.values())

# This solution runs in O(N * K) time and O(N * K) space complexity where N is the number of words in the input list and 
# K is the maximum length of a word. This is because we iterate through each of the N words, and for each word, we build a 
# character frequency map which takes O(K) time. The space complexity is also O(N * K) in the worst case, where all words 
# are anagrams of each other, resulting in a single entry in the dictionary with a list of all N words.