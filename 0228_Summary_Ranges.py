from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        ret = []
        start = [nums[0]]
        for i in range(1, len(nums)):
            if start[-1] + 1 != nums[i]:
                if len(start) == 1:
                    ret.append(str(start[0]))
                else:
                    ret.append(str(start[0]) + "->" + str(start[-1]))
                start = []
            if len(start) == 2:
                start[-1] = nums[i]
            else:
                start.append(nums[i])
                
        if len(start) == 1:
            ret.append(str(start[0]))
        else:
            ret.append(str(start[0]) + "->" + str(start[-1]))

        return ret

# This solution runs in O(n) time complexity where n is the length of the input list nums. This is because it iterates
# through the list once. When there is a break in the consecutive sequence, it appends the current range to the result
# list which is an O(1) operation. Thus, the overall time complexity remains O(n). It then clears the list used to track
# the current range and continues processing the rest of the list. The space complexity is also O(1) without counting the
# output list, since it uses a fixed amount of extra space regardless of the input size.