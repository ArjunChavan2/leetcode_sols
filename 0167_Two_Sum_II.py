class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            
        return [left + 1, right + 1]
    
    
# This solution runs in O(n) time complexity where n is the length of the input list "numbers".
# It uses a two-pointer approach, starting with one pointer at the beginning and one at the end of the list.
# It then iterates through the list, increasing the left pointer when the sum is too small and decreasing the
# right pointer when the sum is too large, until the sum equals the target value. The sum returns the indices of
# the two elements that sum to the target value, with indices starting at 1 instead of 0.