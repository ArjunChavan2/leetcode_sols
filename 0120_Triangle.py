from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = [[triangle[0][0]]]
        if(len(triangle) < 2):
            return memo[0][0]
        memo.append([triangle[1][0] + triangle[0][0], triangle[1][1] + triangle[0][0]])
        for i in range(2, len(triangle)):
            memo.append([memo[i-1][0] + triangle[i][0]])
            for j in range(1, i):
                memo[i].append(min(memo[i-1][j-1],memo[i-1][j]) + triangle[i][j])
            memo[i].append(memo[i-1][-1] + triangle[i][-1])

        return min(memo[-1])


# This solution runs in O(n^2) time complexity where n is the number of rows in the triangle. This is because it uses
# a nested loop structure: the outer loop iterates through each row of the triangle, and for each row, the inner loop 
# iterates through the elements of that row to compute the minimum path sums. The total number of operations performed 
# is proportional to the sum of the first n integers, which is (n * (n + 1)) / 2, leading to an overall time complexity 
# of O(n^2). The space complexity is also O(n^2) because the memoization table 'memo' stores the minimum path sums for 
# each element in the triangle, resulting in a total of (n * (n + 1)) / 2 elements stored in the list.