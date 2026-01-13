from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ret = [0] * n

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ret[stack[-1]] = i - stack[-1]
                del stack[-1]
            
            stack.append(i)
        
        return ret
            
# This solution runs in O(n) time and O(n) space complexity where n is the length of the temperatures list.
# This is because each temperature is processed at once and each index is pushed and popped from the stack at most once.
# The space complexity is O(n) due to the storage of the result list and the stack, which in the worst case can hold all
# indices if the temperatures are in decreasing order.