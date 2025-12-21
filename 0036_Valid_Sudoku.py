from typing import List
class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic = {}
        
        for x in range(0, 9):
            for i in range(1, 10):
                dic[i] = 0
            for y in range(0, 9):
                if(board[x][y] != '.'):
                    dic[int(board[x][y])] += 1
            if max(dic.values()) >= 2:
                return False

        
        for y in range(0, 9):
            for i in range(1, 10):
                dic[i] = 0
            for x in range(0, 9):
                if(board[x][y] != '.'):
                    dic[int(board[x][y])] += 1
            if max(dic.values()) >= 2:
                return False
        
        check = []
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                check = []
                for i in range(x, x + 3):
                    for j in range(y, y + 3):
                        if board[i][j] != '.':
                            check.append(board[i][j])
                if len(set(check)) != len(check):
                    return False
                

        return True

# This solution runs in O(1) time complexity, as it always checks a fixed 9x9 board.
# The space complexity is also O(1) because the dictionary and check list have a fixed size of 9 elements each.
# The solution checks for one thing, every number in every row, column, and 3x3 grid is unique.