class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #memo represents the number of paths possible to reach (x_i, y_i)

        memo = [[1 for _ in range(m + 1)] for _ in range(n + 1)]

        for row in range(1, n + 1):
            for col in range(1, m + 1):
                memo[row][col] = memo[row - 1][col] + memo[row][col - 1]
        
        for i in memo:
            print(i)
        return memo[-2][-2]

# The time complexity of the above code is O(m*n) and the space complexity is O(m*n) because we are 
# using a 2D array of size (m+1)*(n+1) to store the memoized values. Each cell adds the ways to 
# reach that cell from the top and left cells. The final answer is stored in memo[n-1][m-1].