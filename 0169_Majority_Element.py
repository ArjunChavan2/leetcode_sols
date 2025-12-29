from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ind = set(nums)
        for i in ind:
            if nums.count(i) > len(nums) / 2:
                return i

# This solution runs in O(n^2) time complexity where n is the length of the input list nums. This is because for each
# unique element in the list (which can be up to n in the worst case), it counts its occurrences in the list, which takes O(n) time.
# Therefore, the overall time complexity is O(n^2). The space complexity is O(k), where k is the number of unique elements in the list,
# due to the storage of the set of unique elements. In the worst case, k can be equal to n, leading to O(n) space complexity.