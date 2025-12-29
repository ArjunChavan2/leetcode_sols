class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            temp = 0
            for d in range(0, len(str(num))):
                temp += int(str(num)[d])
            num = temp
        
        return num

# This solution runs in O(log n) time complexity where n is the input number. This is because the number of digits in the number
# decreases with each iteration of the while loop, and the number of digits is proportional to log(n). The space complexity is O(1)
# because it uses a fixed amount of extra space regardless of the input size.