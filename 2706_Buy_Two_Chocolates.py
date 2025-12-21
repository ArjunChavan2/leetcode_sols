class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices.sort()
        diff = money - prices[0] - prices[1]
        if diff >= 0:
            return diff
        else:
            return money

# This solution runs in O(n log n) runtime and uses O(1) space complexity. This is because the sorting operation
# takes O(n log n) time and the subsequent operations take O(1) time. The space complexity is O(1) because we are
# only using a constant amount of extra space to store the sorted prices and the difference between the money and the
# cost of the two cheapest chocolates.