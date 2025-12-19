class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = -1
        sell = -1
        potentialBuy = -1
        
        for i in prices:
            if buy > -1 and i > sell:
                sell = i
            
            if potentialBuy == -1 or potentialBuy > i:
                potentialBuy = i
            
            if potentialBuy > -1 and sell == -1:
                if i > potentialBuy:
                    buy = potentialBuy
                    sell = i
                    potentialBuy = -1
                else:
                    potentialBuy = i

            elif((i - potentialBuy) - (sell - buy) > 0):
                temp = buy
                buy = potentialBuy
                potentialBuy = -1
                sell = i
            print(i, potentialBuy, buy, sell)
        return sell - buy

# This solution runs in O(n) time and uses O(1) space. It iterates through the list of prices once, and at each step,
# it updates the potential buy price, the buy price, and the sell price based on the current price and the previous values.
# The potential buy price is updated if the current price is lower than the previous potential buy price.
# The buy price and sell price are updated if the current price is higher than the potential buy price and the difference 
# between the current price and the potential buy price is greater than the difference between the sell price and the buy price.
# The final profit is calculated as the difference between the sell price and the buy price.