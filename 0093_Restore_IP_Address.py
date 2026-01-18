from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        nums = []
        l = len(s)
        def backtrack(perm, idx):
            if perm[-1] < 0 or perm[-1] > 255 or idx > l or len(perm) > 4:
                return

            if len(perm) == 4 and idx == l:
                nums.append(perm[:])
                return
            
            if idx == l:
                return

            if perm[-1] == 0:
                perm.append(int(s[idx]))
                backtrack(perm, idx + 1)
            
            else:
                perm[-1] = perm[-1] * 10 + int(s[idx])
                backtrack(perm, idx + 1)
                
                perm[-1] //= 10
                perm.append(int(s[idx]))
                backtrack(perm, idx + 1)
            del perm[-1]
        
        backtrack([int(s[0])], 1)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                nums[i][j] = str(nums[i][j])
            nums[i] = ".".join(nums[i])
        return sorted(nums)

# This solution runs in O(n!) time and O(n!) space where n is the length of string s. This is because the algorithm uses 
# backtracking to find every possible permutation of the input string s. In the worst case, there can be factorial number
# of valid IP addresses that can be formed from the string, leading to O(n!) time complexity. The space complexity is also 
# O(n!) to store all the valid IP addresses in the result list.