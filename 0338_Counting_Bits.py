from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        d = []
        for i in range(n + 1):
            d.append(str(bin(i)).count('1'))

        return d

# This solution runs in O(n log n) time complexity where n is the input number. This is because for each number from 0 to n,
# we convert the number to its binary representation using bin(i), which takes O(log i) time. Since we do this for n numbers, 
# the overall time complexity becomes O(n log n).