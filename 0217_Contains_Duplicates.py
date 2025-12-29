from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return len(s) != len(nums)

# This solution runs in O(n) time complexity where n is the length of the input list nums. This is because creating a set from the list
# involves iterating through the list once to add each element to the set, which takes O(n) time. The space complexity is also O(n) in the worst case,
# as the set may store all n elements if there are no duplicates, leading to O(n) space complexity.