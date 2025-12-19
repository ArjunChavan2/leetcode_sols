class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = grid

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    continue
                elif row == 0:
                    dp[0][col] += dp[0][col - 1]
                elif col == 0:
                    dp[row][0] += dp[row - 1][0]
                else:
                    dp[row][col] += min(dp[row - 1][col], dp[row][col - 1])
        return dp[-1][-1]

# This solution runs in O(m*n) time complexity and uses O(1) space complexity.
# The solution modifies the input grid in place to store the minimum path sum up to each cell.