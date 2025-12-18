class Solution:
    def myAtoi(self, s: str) -> int:
        val = 0
        numStarted = False
        pos = True
        signed = 0
        intStart = 0
        intEnd = len(s)

        for c in range(len(s)):
            if s[c] == ' ':
                if numStarted:
                    intEnd = c
                    break
                continue
            
            if s[c] == '-':
                if(numStarted or signed == 1):
                    intEnd = c
                    break
                pos = False
                numStarted = True
                signed += 1
                intStart = c+1
                continue
            
            if s[c] == '+':
                if(numStarted or signed == 1):
                    intEnd = c
                    break
                pos = True
                numStarted = True
                signed += 1
                intStart = c+1
                continue

            if s[c].isdigit():
                if(numStarted == False):
                    intStart = c
                numStarted = True
                continue
            else:
                intEnd = c
                break
        
        if(intStart == intEnd or not numStarted):
            return 0

        s = s[intStart:intEnd][::-1]
        print(s)
            
        for i in range(0, len(s)):
            val += int(s[i]) * 10**(i)


        if not pos:
            val *= -1
        
        if val > 2**31 - 1:
            val = 2**31 - 1
        elif val < -2**31:
            val = -2**31
        
        return val