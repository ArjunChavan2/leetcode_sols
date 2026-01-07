from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    
        ret = []
        idx = 0
        n = len(candidates)
        def backtrack(perm, s, idx):
            if idx >= n or s >= target:
                if s == target:
                    ret.append(perm[:])
                return
            
            perm.append(candidates[idx])
            backtrack(perm, s + candidates[idx], idx)
            perm.pop()

            backtrack(perm, s, idx + 1)
        
        backtrack([],0, 0)
        return ret
