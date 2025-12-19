class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        memo = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        if(obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1):
            return 0
        for row in range(0, len(obstacleGrid)):
            for col in range(0, len(obstacleGrid[0])):
                if row == 0 and col == 0:
                    memo[0][0] = 1
                elif obstacleGrid[row][col] == 1:
                    memo[row][col] = 0
                elif row == 0:
                    memo[row][col] = memo[row][col - 1]
                elif col == 0:
                    memo[row][col] = memo[row - 1][col]
                else:
                    memo[row][col] = memo[row-1][col] + memo[row][col-1]
        
        for i in memo:
            print(i)
        return memo[-1][-1]

# This solution runs in O(m*n) time and O(m*n) space, where m is the number of rows and n is the 
# number of columns in the obstacleGrid. This is because we are using a 2D array to store the 
# number of unique paths to each cell in the grid, and we are iterating through each cell in the
# grid once. The space complexity is also O(m*n) because we are using a 2D array to store the 
# number of unique paths to each cell in the grid.