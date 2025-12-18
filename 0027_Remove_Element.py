class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        counter = 0
        numVal = nums.count(val)
        for x in range(numVal):
            nums.remove(val)
            counter+=1
            nums.append("*")
        return len(nums) - counter

# This solution has a time complexity of O(n), where n is the length of the input list nums.
# The algorithm iterates through the list to count and remove occurrences of the specified value val.
# Each removal operation takes O(n) time in the worst case, but since the number of
# occurrences of val is limited to the number of elements in the list, the overall time complexity
# remains linear with respect to the size of the input list.