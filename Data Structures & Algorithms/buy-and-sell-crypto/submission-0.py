class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # pointer solution
        # O(n) time
        # O(1) space
        maxProfit = 0
        firstBuy = prices[0]

        for stock in prices:
            maxProfit = max(maxProfit, stock - firstBuy)
            firstBuy = min(firstBuy, stock)
        
        return maxProfit