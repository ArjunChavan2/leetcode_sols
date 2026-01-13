from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]

# This solution runs in O(1) time and O(1) space complexity. The temperature conversion formulas are applied directly
# without any loops or recursive calls, resulting in constant time complexity. The space complexity is also
# constant since only a fixed amount of space is used for the output list regardless of the input size.