class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ret = []

        def backtrack(index, path):
            if index == len(nums):
                ret.append(path[:])
                return
            
            path.append(nums[index])
            backtrack(index + 1, path)
            del path[-1]
            
            backtrack(index + 1, path)
        
        backtrack(0, [])

        return ret

# The solution runs in O(2^n) time and uses O(n) space. The time complexity is 2^n because for each element
# in the list, there are two choices, include it in the subset or don't. This solution uses backtracking to 
# generate all possible subsets by making that choice and backtracking to the previous state and continuing
# with the next choice. The space complexity is n because the maximum depth of the recursion tree is n, which
# is the length of the input list. The space used by the path list is also n in the worst case, but this is
# not counted in the space complexity because it is part of the output. The space used by the ret list is also
# n in the worst case, but this is also not counted in the space complexity because it is part of the output.