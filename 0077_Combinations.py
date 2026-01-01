from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []


        def backtrack(comb, m):
            if len(comb) == k:
                ret.append(comb[:])
                return
            
            for i in range(m, n + 1):
                comb.append(i)
                backtrack(comb, i + 1)
                del comb[-1]
            
        
        backtrack([], 1)
        return ret

# This solution runs in O(C(n, k) * k) time complexity where C(n, k) represents the number of combinations.
# This is because we generate all possible combinations of size k from n elements, and for each combination, we 
# perform O(k) operations to copy it to the result list. The space complexity is also O(C(n, k) * k) because we 
# store all the combinations in the output list, and each combination has k elements.