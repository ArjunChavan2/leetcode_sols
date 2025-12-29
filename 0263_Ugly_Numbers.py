class Solution:
    def isUgly(self, n: int) -> bool:
        while n % 2 == 0 and n > 1:
            n = n // 2
        
        while n % 3 == 0 and n > 1:
            n = n // 3
        
        while n % 5 == 0 and n > 1:
            n = n // 5
        
        return n == 1
        
# This solution runs in O(log n) time complexity where n is the input number. This is because the number of times
# we can divide n by 2, 3, or 5 is proportional to log(n). The space complexity is O(1) because it uses a fixed 
# amount of extra space regardless of the input size.