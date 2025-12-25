from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        for i in range(2, numRows + 1):
            row = [int(d) for d in str(10**(i-1) + 1)]
            for j in range(1, i-1):
                row[j] = ret[i-2][j-1]+ret[i-2][j]
            ret.append(row)
            
        return ret

# This solution runs in O(numRows^2) time complexity because it uses a nested loop structure:
# the outer loop iterates numRows - 1 times (from 2 to numRows), and for each iteration of the outer loop,
# the inner loop iterates up to i-2 times, where i is the current row number. The total number of operations
# performed is proportional to the sum of the first numRows integers, which is (numRows * (numRows - 1)) / 2,
# leading to an overall time complexity of O(numRows^2). The space complexity is also O(numRows^2) because the 
# output list 'ret' contains numRows rows, and each row i contains i elements, resulting in a total of 
# (numRows * (numRows + 1)) / 2 elements stored in the list.