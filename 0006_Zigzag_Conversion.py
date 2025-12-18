class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row = [""]* numRows
        b = True
        while b:
            for i in range(0, numRows):
                if(len(s) == 0):
                    b = False
                    break
                
                row[i] += s[0]
                s = s[1::]
            

            for i in range(numRows - 2, 0, -1):
                if(len(s) == 0):
                    b = False
                    break
                
                row[i] += s[0]
                s = s[1::]
    
        return "".join(row)

# This solution has a time complexity of O(n) where n is the length of the input string s.
# The algorithm iterates through each character of the string exactly once,
# appending it to the appropriate row in a zigzag pattern. The final join operation
# also takes O(n) time, resulting in an overall linear time complexity.